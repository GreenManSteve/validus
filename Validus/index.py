import uuid

from database import DataBase
from Scripts.data_fund import DataFund
from Scripts.data_commitment import DataCommitment
from Scripts.data_call import DataCall
from Scripts.data_fund_investment import DataFundInvestment
from Scripts.investment import Investment
from Scripts.validus_composite import ValidusComposite



# Reset The example:
data_commit = DataCommitment()
data_call = DataCall()
data_fund_investment = DataFundInvestment()

data_commit.reset_example()
data_call.reset_example()
data_fund_investment.reset_example()

