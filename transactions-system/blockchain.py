"""
Blockchain used in transactions system.

Usage:

create Chain object.
>>> chain = Chain()
or, if there is exported chain
>>> chain = Chain("path/to/exported/chain.")

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

At any moment, you can validate chain as every block has
a HASH dynamically generated according to it's data, so 
any change made to block changes it's HASH. Every next
block contains HASH of previous.
>>> chain.validate_stack()
this method checks data of every block and compares HASHES.
If any block has been changed, stack will be truncated removing
all blocks ahead including changed one.

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
    

class Chain:
    """ Connects blocks, assigns previous hashes to new blocks. 
    Only one instance of Chain can exists at once. When instance
    actually exists, creating new instances will return currently 
    existing one. """
    instance: "Chain" = None

    def __init__(self, file_path=None) -> None:
        if Chain.instance is not None:
            logger.debug("Chain: Tried to create new instance of Chain, returned existing one.")
            self = Chain.instance
            return
        
        if file_path is not None:
            logger.info("Chain: Generating Chain instance from provided file's path.")
            self._import_chain(file_path)
            return

        initial_block = Block("", "", "", -1)
        initial_block.previous_hash = "0" * 64
        self.stack: list[Block] = [initial_block]
        Chain.instance = self
        logger.info("Chain: Created Chain instance.")

    def get_previous_hash(self) -> str:
        """ Get hash of last block. """
        return self.stack[-1].generate_hash()
    
    def append_block(self, block: Block):
        """ Add new block to stack and assign 
        previous hash according to last block. """
        block.previous_hash = self.get_previous_hash()
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
        """ Check if previous hash is matching with actual
        hash of previous block. """
        self.display_stack()
        for index, block in enumerate(self.stack):
            if index == len(self.stack)-1:
                logger.info("Chain: Stack validation passed successfully")
                return True
            
            if self.stack[index+1].previous_hash != block.generate_hash():
                invalid_block = self.stack[index+1]
                removed_blocks_amount = len(self.stack[index+1:])
                self.stack = self.stack[0:index]
                logger.error(f"Chain: Found invalid block in stack. Stack has been shortened by {removed_blocks_amount} blocks (HASH:{invalid_block.generate_hash()})")
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

    def _import_chain(self, path: str) -> None:
        """ Generate chain with blocks from exported file. 
        This function is called when file_path is provided
        at Chain creation. """
        if not os.path.exists(path):
            raise FileExistsError(path)

        if Chain.instance is not None:
            raise PermissionError("Cannot import chain when actually exists.")

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
        
        self.stack = stack
        logger.info(f"Chain: Import: imported {len(stack)} blocks, validating data...")
        self.validate_stack()

    def display_stack(self):
        """ Display all blocks in this chain. (hash, previous_hash, seller_id, offer_id, buyer_id, price) """
        for block in self.stack:
            print(f"H={block.generate_hash()} PRE_H={block.previous_hash} SID={block.seller_id} OID={block.offer_id} BID={block.buyer_id} PR={block.price}")
