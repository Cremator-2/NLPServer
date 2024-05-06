# NLPServer

## Project tree

```
├─── app/
│    ├─── api/
│    │    ├─── api_v1/
│    │    │    ├─── healthcheck/
│    │    │    │    ├─── models.py
│    │    │    │    └─── routes.py
│    │    │    ├─── processing/
│    │    │    │    ├─── models.py
│    │    │    │    ├─── processing.py
│    │    │    │    └─── routes.py
│    │    │    ├─── similarity/
│    │    │    │    ├─── models.py
│    │    │    │    └─── routes.py
│    │    │    └─── __init__.py
│    │    └─── __init__.py
│    ├─── core/
│    │    └─── config.py
│    ├─── notebooks/
│    │    ├─── IMDB Dataset.csv
│    │    ├─── IMDB.ipynb
│    ├─── routers/
│    │    ├─── __init__.py
│    │    ├─── page_router.py
│    │    └─── plot_router.py
│    ├─── static/
│    │    ├─── ml_models/
│    │    │    ├─── lr_tfidf_model.joblib
│    │    │    └─── tfidf_vectorizer.joblib
│    │    ├─── pages/
│    │    │    └─── example_chat.html
│    │    └─── plots/
│    │         └─── example_plot.html
│    ├─── tests/
│    │    ├─── classificator_endpoint.py
│    │    ├─── healthcheck.py
│    │    ├─── preprocessing_endpoint.py
│    │    ├─── preprocessing_obj.py
│    │    └─── similarity.py
│    ├─── utils/
│    │    └─── logger/
│    │         ├─── __init__.py
│    │         ├─── custom_formatter.py
│    │         └─── logger.py
│    └─── main.py
├─── README.md
└─── requirements.txt
```
