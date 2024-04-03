# NLPServer

## Project tree

```
├─── requirements.txt
└─── app/
     ├─── main.py
     ├─── api/
     │    ├─── __init__.py
     │    └─── api_v1/
     │         ├─── __init__.py
     │         └─── healthcheck/
     │              └─── routes.py
     ├─── core/
     │    └─── config.py
     ├─── routers/
     │    ├─── __init__.py
     │    ├─── page_router.py
     │    └─── plot_router.py
     ├─── static/
     │    ├─── pages/
     │    └─── plots/
     ├─── templates/
     ├─── tests/
     │    └─── healthcheck.py
     └─── utils/
          └─── logger/
               ├─── __init__.py
               ├─── custom_formatter.py
               └─── logger.py
```
