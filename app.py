{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "e64f5348",
   "metadata": {},
   "outputs": [],
   "source": [
    "from flask import Flask, render_template, request"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "c54385cb",
   "metadata": {},
   "outputs": [],
   "source": [
    "import joblib"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "84a7e78a",
   "metadata": {},
   "outputs": [],
   "source": [
    "app = Flask(__name__)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "0e58bb72",
   "metadata": {},
   "outputs": [],
   "source": [
    "@app.route(\"/\",methods=[\"GET\",\"POST\"])\n",
    "def index():\n",
    "    if request.method == \"POST\":\n",
    "        rates = float(request.form.get(\"rates\"))\n",
    "        model1 = joblib.load(\"regression\")\n",
    "        pred1 = model1.predict([[rates]])\n",
    "        model2 = joblib.load(\"decision_tree\")\n",
    "        pred2 = model2.predict([[rates]])\n",
    "\n",
    "        return(render_template(\"index.html\", result1 = pred1, result2 = pred2))\n",
    "    else:\n",
    "        return(render_template(\"index.html\", result1=\"WAITING\", result2=\"WAITING\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "aed5f433",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app \"__main__\" (lazy loading)\n",
      " * Environment: production\n",
      "\u001b[31m   WARNING: This is a development server. Do not use it in a production deployment.\u001b[0m\n",
      "\u001b[2m   Use a production WSGI server instead.\u001b[0m\n",
      " * Debug mode: off\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      " * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)\n",
      "127.0.0.1 - - [06/Jul/2022 17:10:33] \"GET / HTTP/1.1\" 200 -\n",
      "D:\\ANACONDA\\anaconda\\lib\\site-packages\\sklearn\\base.py:450: UserWarning: X does not have valid feature names, but LinearRegression was fitted with feature names\n",
      "  warnings.warn(\n",
      "D:\\ANACONDA\\anaconda\\lib\\site-packages\\sklearn\\base.py:450: UserWarning: X does not have valid feature names, but DecisionTreeRegressor was fitted with feature names\n",
      "  warnings.warn(\n",
      "127.0.0.1 - - [06/Jul/2022 17:10:38] \"POST / HTTP/1.1\" 200 -\n",
      "D:\\ANACONDA\\anaconda\\lib\\site-packages\\sklearn\\base.py:450: UserWarning: X does not have valid feature names, but LinearRegression was fitted with feature names\n",
      "  warnings.warn(\n",
      "D:\\ANACONDA\\anaconda\\lib\\site-packages\\sklearn\\base.py:450: UserWarning: X does not have valid feature names, but DecisionTreeRegressor was fitted with feature names\n",
      "  warnings.warn(\n",
      "127.0.0.1 - - [06/Jul/2022 17:10:43] \"POST / HTTP/1.1\" 200 -\n"
     ]
    }
   ],
   "source": [
    "if __name__ == \"__main__\":\n",
    "    app.run()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b6aa6173",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
