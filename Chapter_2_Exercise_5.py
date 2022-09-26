{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNOIA3lSW2KAPmhNVN+aGFj",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/xtrnals/Chapter-2/blob/main/Chapter_2_Exercise_5.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 12,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "3BzlRva65Ge4",
        "outputId": "6d20069a-fdaa-4526-9395-b0dc205e7dc4"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "You can get 8 usbs\n",
            "and your change will be 2 pounds\n"
          ]
        }
      ],
      "source": [
        "money = 50\n",
        "usb = int(money / 6)\n",
        "print(\"You can get\", usb, \"usbs\")\n",
        "change = int(money % 6)\n",
        "print (\"and your change will be\", change, \"pounds\")\n"
      ]
    }
  ]
}