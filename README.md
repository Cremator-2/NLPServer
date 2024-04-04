# NLPServer

## Project tree

```
├─── app/
│    ├─── api/
│    │    ├─── api_v1/
│    │    │    ├─── healthcheck/
│    │    │    │    ├─── models.py
│    │    │    │    └─── routes.py
│    │    │    └─── __init__.py
│    │    └─── __init__.py
│    ├─── core/
│    │    └─── config.py
│    ├─── routers/
│    │    ├─── __init__.py
│    │    ├─── page_router.py
│    │    └─── plot_router.py
│    ├─── static/
│    │    ├─── pages/
│    │    │    └─── example_chat.html
│    │    └─── plots/
│    │         └─── example_plot.html
│    ├─── tests/
│    │    └─── healthcheck.py
│    ├─── utils/
│    │    └─── logger/
│    │         ├─── __init__.py
│    │         ├─── custom_formatter.py
│    │         └─── logger.py
│    └─── main.py
└─── requirements.txt
```
