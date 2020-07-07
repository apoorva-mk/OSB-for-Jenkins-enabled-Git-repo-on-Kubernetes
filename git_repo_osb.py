from typing import Union, List

import openbrokerapi
from openbrokerapi.api import ServiceBroker
from openbrokerapi.catalog import ServicePlan
from openbrokerapi.service_broker import (
    Service,
    ProvisionDetails,
    ProvisionedServiceSpec,
    DeprovisionDetails,
    DeprovisionServiceSpec,
    ProvisionState
)


class MyServiceBroker(ServiceBroker):
    def catalog(self) -> Union[Service, List[Service]]:
        return Service(
            id='1',
            name='Jenkins enables git repository',
            description='Create a git repository with a jenkins job enabled',
            bindable=False,
            plans=[
                ServicePlan(
                    id='1',
                    name='Plan 1',
                    description='Create a git repository with a jenkins job enabled',
                )
            ]
        )

    def provision(self,
                  instance_id: str,
                  details: ProvisionDetails,
                  async_allowed: bool,
                  **kwargs) -> ProvisionedServiceSpec:
        # Create service instance
        # ...

        return ProvisionedServiceSpec(state=ProvisionState.IS_ASYNC,
            operation='provision', dashboard_url="http://github.com")

    def deprovision(self,
                    instance_id: str,
                    details: DeprovisionDetails,
                    async_allowed: bool,
                    **kwargs) -> DeprovisionServiceSpec:
        # Delete service instance
        # ...

        return DeprovisionServiceSpec(is_async=False)

print('Start server on 127.0.0.1:5000')
print('Check the catalog at:')
#print('> curl 127.0.0.1:5000/v2/catalog -H "X-Broker-API-Version: 2.14"')
openbrokerapi.api.serve(MyServiceBroker(), None)