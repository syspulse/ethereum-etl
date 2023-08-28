# MIT License
#
# Copyright (c) 2018 Evgeny Medvedev, evge.medvedev@gmail.com
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


from ethereumetl.domain.transaction_fat import EthTransactionFat
from ethereumetl.utils import hex_to_dec, to_normalized_address


class EthTransactionFatMapper(object):

    def json_dict_to_transaction(self, json_dict, **kwargs):
        transaction = EthTransactionFat()

        transaction.hash = json_dict.get('hash')
        transaction.nonce = hex_to_dec(json_dict.get('nonce'))
        transaction.block_hash = json_dict.get('blockHash')
        transaction.block_number = hex_to_dec(json_dict.get('blockNumber'))
        transaction.block_timestamp = kwargs.get('block_timestamp')
        transaction.transaction_index = hex_to_dec(json_dict.get('transactionIndex'))
        transaction.from_address = to_normalized_address(json_dict.get('from'))
        transaction.to_address = to_normalized_address(json_dict.get('to'))
        transaction.value = hex_to_dec(json_dict.get('value'))
        transaction.gas = hex_to_dec(json_dict.get('gas'))
        transaction.gas_price = hex_to_dec(json_dict.get('gasPrice'))
        transaction.input = json_dict.get('input')
        transaction.max_fee_per_gas = hex_to_dec(json_dict.get('maxFeePerGas'))
        transaction.max_priority_fee_per_gas = hex_to_dec(json_dict.get('maxPriorityFeePerGas'))
        transaction.transaction_type = hex_to_dec(json_dict.get('type'))
        
        return transaction

    
    def transaction_fat_to_dict(self, block, transaction,receipt,logs):
        return {
            #'type': 'transaction',
            'type': 'tx',

            # --------------------------------- Block
            'block_parent_hash': block.parent_hash,
            'block_nonce': block.nonce,
            'block_sha3_uncles': block.sha3_uncles,
            'block_logs_bloom': block.logs_bloom,
            'block_transactions_root': block.transactions_root,
            'block_state_root': block.state_root,
            'block_receipts_root': block.receipts_root,
            'block_miner': block.miner,
            'block_difficulty': block.difficulty,
            'block_total_difficulty': block.total_difficulty,
            'block_size': block.size,
            'block_extra_data': block.extra_data,
            'block_gas_limit': block.gas_limit,
            'block_gas_used': block.gas_used,
            'block_timestamp': block.timestamp,
            'block_base_fee_per_gas': block.base_fee_per_gas,

            # ----------------------------------- Tx + Receipt
            'hash': transaction.hash,
            'nonce': transaction.nonce,
            'block_hash': transaction.block_hash,
            'block_number': transaction.block_number,
            'block_timestamp': transaction.block_timestamp,
            'transaction_index': transaction.transaction_index,
            'from_address': transaction.from_address,
            'to_address': transaction.to_address,
            'value': transaction.value,
            'gas': transaction.gas,
            'gas_price': transaction.gas_price,
            'input': transaction.input,
            'max_fee_per_gas': transaction.max_fee_per_gas,
            'max_priority_fee_per_gas': transaction.max_priority_fee_per_gas,
            
            'cumulative_gas_used': receipt.cumulative_gas_used,
            'gas_used': receipt.gas_used,
            'contract_address': receipt.contract_address,
            'root': receipt.root,
            'status': receipt.status,
            'effective_gas_price': receipt.effective_gas_price,

            'transaction_type': transaction.transaction_type,

            # -------------------------------------- Logs
            'logs': logs
        }
