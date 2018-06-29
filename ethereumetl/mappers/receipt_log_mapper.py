from ethereumetl.domain.receipt_log import EthReceiptLog
from ethereumetl.utils import hex_to_dec


class EthReceiptLogMapper(object):

    def json_dict_to_receipt_log(self, json_dict):
        receipt_log = EthReceiptLog()

        receipt_log.log_index = hex_to_dec(json_dict.get('logIndex', None))
        receipt_log.transaction_hash = json_dict.get('transactionHash', None)
        receipt_log.transaction_index = hex_to_dec(json_dict.get('transactionIndex', None))
        receipt_log.block_hash = json_dict.get('blockHash', None)
        receipt_log.block_number = hex_to_dec(json_dict.get('blockNumber', None))
        receipt_log.address = json_dict.get('address', None)
        receipt_log.data = json_dict.get('data', None)
        receipt_log.topics = json_dict.get('topics', None)

        return receipt_log

    def web3_dict_to_receipt_log(self, dict):

        receipt_log = EthReceiptLog()

        receipt_log.log_index = dict.get('logIndex', None)

        transaction_hash = dict.get('transactionHash', None)
        if transaction_hash is not None:
            transaction_hash = transaction_hash.hex()
        receipt_log.transaction_hash = transaction_hash

        block_hash = dict.get('blockHash', None)
        if block_hash is not None:
            block_hash = block_hash.hex()
        receipt_log.block_hash = block_hash

        receipt_log.block_number = dict.get('blockNumber', None)
        receipt_log.address = dict.get('address', None)
        receipt_log.data = dict.get('data', None)

        if 'topics' in dict:
            receipt_log.topics = [topic.hex() for topic in dict['topics']]

        return receipt_log

    def receipt_log_to_dict(self, receipt_log):
        return {
            'type': 'log',
            'log_index': receipt_log.log_index,
            'log_transaction_hash': receipt_log.transaction_hash,
            'log_transaction_index': receipt_log.transaction_index,
            'log_block_hash': receipt_log.block_hash,
            'log_block_number': receipt_log.block_number,
            'log_address': receipt_log.address,
            'log_data': receipt_log.data,
            'log_topics': '|'.join(receipt_log.topics)
        }