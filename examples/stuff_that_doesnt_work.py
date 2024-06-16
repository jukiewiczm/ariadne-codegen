from examples.graphql_client import Client, PluginFilterInput, PluginStatusInChannelsInput
from examples.graphql_client.custom_fields import PluginCountableConnectionFields
from examples.graphql_client.custom_queries import Query

if __name__ == '__main__':
    client = Client()
    client.query(
        Query.plugins(
            filter=PluginFilterInput(
                status_in_channels=PluginStatusInChannelsInput(
                    active=True, channels=["channel1"]
                )
            )
        )
        .fields(
            PluginCountableConnectionFields.total_count
        ),
        operation_name="op"
    )