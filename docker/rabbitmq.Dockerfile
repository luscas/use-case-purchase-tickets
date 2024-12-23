FROM rabbitmq:management

RUN rabbitmq-plugins enable --offline \
  rabbitmq_management_agent \
  rabbitmq_management \
  rabbitmq_prometheus
