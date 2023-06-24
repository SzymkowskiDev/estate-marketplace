from typing import Callable, List
import hashlib
import logging
import os

logger = logging.getLogger(__name__)
logging.basicConfig(format='%(asctime)s <%(levelname)s> %(message)s', datefmt='[%m/%d/%Y %H:%M:%S]')
logger.setLevel(logging.DEBUG)
logger.debug("Blockchain's logger initialized.")


class Block:
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
        return (self.generate_hash(), self.previous_hash, self.seller_id, self.buyer_id, self.offer_id, self.price) 

    def generate_data_chain(self) -> str:
        if self.previous_hash is None:
            raise ValueError("Block is not ready yet.")
        data = f"~~{self.seller_id}--{self.buyer_id}--{self.offer_id}--{self.price}--{self.previous_hash}"
        return data

    def generate_hash(self) -> str:
        data = self.generate_data_chain()
        hashed_data = hashlib.sha256(data.encode()).hexdigest()
        return hashed_data


def default_validation_error_handler(blocks: List[Block]) -> None:
    logger.info("=== BLOCKS AFFECTED BY VALIDATION ERROR ===")
    for block in blocks:
        logger.info(f" > {block.generate_data_chain()}")
    logger.info("=== END OF OUTPUT ===")


class Chain:
    instance: "Chain" = None
    on_validation_error: Callable = default_validation_error_handler

    @staticmethod
    def build_from_file(path: str) -> "Chain":
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
        return self.stack[-1].generate_hash()
    
    def append_block(self, block: Block):
        block.previous_hash = self.get_latest_hash()
        self.stack.append(block)
        logger.info(f"Chain: new block added (HASH:{block.generate_hash()})")

    def bulk_append(self, *blocks: Block):
        for block in blocks:
            if isinstance(block, Block):
                self.append_block(block)
            else:
                logger.warning(f"Chain: (bulk_append) Invalid object found in data stack: (TYPE:{type(block)})")

    def validate_stack(self) -> bool:
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
        if len(self.stack) == 0:
            return
        
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
        for block in self.stack:
            print(f"H={block.generate_hash()} PRE_H={block.previous_hash} SID={block.seller_id} OID={block.offer_id} BID={block.buyer_id} PR={block.price}")
