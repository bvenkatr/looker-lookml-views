import json
import looker_sdk

from looker_sdk.api40.methods import Looker40SDK

sdk: Looker40SDK = looker_sdk.init40()

result_str = sdk.run_look(
    look_id ="5",
    result_format = "json"
)

result = json.loads(result_str)
