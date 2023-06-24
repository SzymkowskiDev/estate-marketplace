"""
Blockchain used in transactions system.
@gental-py

Usage:

create Chain object.
>>> chain = Chain()
or, if there is exported chain
>>> chain = Chain.build_from_file("path/to/exported/stack/")

when there is transaction, create block.
seller_id: 0, buyer_id: 1, offer_id: 2, price: 100
>>> block = Block(0, 1, 2, 100)
now, add this block to chain.
>>> chain.append_block(block)
or, You can safely use new Chain instance
>>> Chain().append_block(block)

You can also add more than one block using another method
>>> block1 = Block(1, 1, 1, 100)
>>> block2 = Block(2, 2, 2, 200)
>>> block3 = Block(3, 3, 3, 300)
>>> chain.bulk_append(block1, block2, block3)

You can validate chain anytime as every block has
a HASH dynamically generated according to it's data, so 
any change made to block changes it's HASH. Every next
block contains original HASH of previous block.
>>> chain.validate_stack()
this method checks data of every block and compares HASHes.
If any block has been changed, stack will be truncated removing
all blocks ahead including changed one. If you want to handle
removed blocks, you can set Chain.on_validation_error object's
variable to an Callble object. It will be called whenever validation
error occures.

To safely save chain's data, You can export it to any file.
>>> chain.export_chain("/path/to/export/")
If path doesn't exists, IT WILL BE CREATED.

If any chain instance exists, creating new ones will return currently
existing instance instead of creating a new one. It means, you can
create as many instances as you want and they will still be the same
as first one created at current session. 

So if instance of Chain was created in current session, then:
>>> chain = Chain()  # first time call
>>> chain == Chain()  # -> True
"""
from typing import Callable, List
import hashlib
import logging
import os

logger = logging.getLogger(__name__)
logging.basicConfig(format='%(asctime)s <%(levelname)s> %(message)s', datefmt='[%m/%d/%Y %H:%M:%S]')
logger.setLevel(logging.DEBUG)
logger.debug("Blockchain's logger initialized.")


class Block:
    """ Block in this blockchain system represents each transaction. 
    previous_hash attribute is set by the chain according to it's data. """
    def __init__(self, seller_id, buyer_id, offer_id, price) -> None:
        self.seller_id = seller_id
        self.buyer_id = buyer_id
        self.offer_id = offer_id
        self.price = price
        self.previous_hash = None

    def __str__(self) -> str:
        return self.generate_hash()

    def __repr__(self) -> str:
        return f"<Block: {self.generate_hash()} content: {self.seller_id} {self.buyer_id} {self.offer_id} {self.price}>"

    def as_tuple(self) -> tuple:
        """ -> (hash, previous_hash, seller_id, buyer_id, offer_id, price) """
        return (self.generate_hash(), self.previous_hash, self.seller_id, self.buyer_id, self.offer_id, self.price) 

    def generate_data_chain(self) -> str:
        """ data_chain content: ~~seller_id--buyer_id--offer_id--price--previous_hash """
        if self.previous_hash is None:
            raise ValueError("Block is not ready yet.")
        data = f"~~{self.seller_id}--{self.buyer_id}--{self.offer_id}--{self.price}--{self.previous_hash}"
        return data

    def generate_hash(self) -> str:
        """ Generate SHA256 hash from block's data chain. """
        data = self.generate_data_chain()
        hashed_data = hashlib.sha256(data.encode()).hexdigest()
        return hashed_data


def default_validation_error_handler(blocks: List[Block]) -> None:
    """ Log data of all removed blocks in validation error. """
    logger.info("=== BLOCKS AFFECTED BY VALIDATION ERROR ===")
    for block in blocks:
        logger.info(f" > {block.generate_data_chain()}")
    logger.info("=== END OF OUTPUT ===")


class Chain:
    """ Connects blocks, assigns previous hashes to new blocks. 
    Only one instance of Chain can exists at once. When instance
    actually exists, creating new instances will return currently 
    existing one. 
    on_validation_error is object's variable used for handling 
    blocks affected (removed) by illegal block. Value must be callable."""
    instance: "Chain" = None
    on_validation_error: Callable = default_validation_error_handler

    @staticmethod
    def build_from_file(path: str) -> "Chain":
        """ Generate chain with blocks from exported file. 
        This function is called when file_path is provided
        at Chain creation. """
        if not os.path.exists(path):
            raise FileNotFoundError(path)

        if Chain.instance is not None:
            raise ValueError("Cannot import chain when actually exists.")

        stack = []
        with open(path, "r") as file:
            content = file.read()

        blocks = content.split("~~")
        for raw_block_data in blocks:
            block_data = raw_block_data.split("--")
            if len(block_data) == 1:
                continue
            seller_id, buyer_id, offer_id, price, previous_hash = block_data
            block = Block(seller_id, buyer_id, offer_id, price)
            block.previous_hash = previous_hash
            stack.append(block)
        
        chain = Chain()
        chain.stack = stack
        logger.info(f"Chain: Build stack from {len(stack)} blocks. Validating data...")
        chain.validate_stack()
        return chain

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = object.__new__(cls, *args, **kwargs)
            logger.info("Chain: Created new Chain.")
        return cls.instance

    def __init__(self) -> None:
        initial_block = Block("", "", "", -1)
        initial_block.previous_hash = "0" * 64
        self.stack: list[Block] = [initial_block]

    def get_latest_hash(self) -> str:
        """ Get hash of last block. """
        return self.stack[-1].generate_hash()
    
    def append_block(self, block: Block):
        """ Add new block to stack and assign 
        previous hash according to last block. """
        block.previous_hash = self.get_latest_hash()
        self.stack.append(block)
        logger.info(f"Chain: new block added (HASH:{block.generate_hash()})")

    def bulk_append(self, *blocks: Block):
        """ Append multiple blocks. """
        for block in blocks:
            if isinstance(block, Block):
                self.append_block(block)
            else:
                logger.warning(f"Chain: (bulk_append) Invalid object found in data stack: (TYPE:{type(block)})")

    def validate_stack(self) -> bool:
        """ Check if previous hash is matching with actual hash of 
        previous block. If on_validation_error variable is set correctly,
        this object will be called with list of illegal blocks as argument. """
        for index, block in enumerate(self.stack):
            if index == len(self.stack)-1:
                logger.info("Chain: Stack validation passed successfully")
                return True
            
            if self.stack[index+1].previous_hash != block.generate_hash():
                invalid_block = self.stack[index+1]
                removed_blocks = self.stack[index:]
                self.stack = self.stack[0:index]
                logger.error(f"Chain: Found invalid block in stack. Stack has been truncated by {len(removed_blocks)} blocks (HASH:{invalid_block.generate_hash()})")
                
                if Chain.on_validation_error is not None:
                    if not isinstance(Chain.on_validation_error, Callable):
                        logger.error("Chain: on_validation_error: This object is not Callable.")
                        return False
                    
                    try:
                        Chain.on_validation_error(removed_blocks)
                        logger.info("Chain: Called on_validation_error.")
                    except TypeError:
                        logger.error("Chain: Failed to call on_validtion_error handler.")

                return False

    def export_chain(self, path: str) -> None:
        """ Export entire stack into file. """
        if not os.path.exists(path):
            try:
                open(path, "a+").close()
                logger.info(f"Chain: Export: Created output file in: {path}")
            except Exception as error:
                logger.error(f"Chain: Export: Failed to create output file in: {path} ({error})")
                return
        
        data = "".join([block.generate_data_chain() for block in self.stack])
        with open(path, "w+") as file:
            file.write(data)
        logger.info(f"Chain: Exported {len(self.stack)} blocks to: {path}")

    def display_stack(self):
        """ Display all blocks in this chain. (hash, previous_hash, seller_id, offer_id, buyer_id, price) """
        for block in self.stack:
            print(f"H={block.generate_hash()} PRE_H={block.previous_hash} SID={block.seller_id} OID={block.offer_id} BID={block.buyer_id} PR={block.price}")
