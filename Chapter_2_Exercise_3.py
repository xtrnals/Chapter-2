{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNPBMXXOQE8SPNAjUquVNTA",
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
        "<a href=\"https://colab.research.google.com/github/xtrnals/Chapter-2/blob/main/Chapter_2_Exercise_3.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 5,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "VvrIlvrX3aUK",
        "outputId": "ceb0ea2c-c892-4fe0-c826-83a145a9fe61"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            " \tJonathan\n",
            " \n",
            "Jonathan\n",
            " \n",
            " \tJonathan\n",
            "Jonathan\n"
          ]
        }
      ],
      "source": [
        "name = \" \\tJonathan\\n \"\n",
        "\n",
        "print (name)\n",
        "print (name.lstrip())\n",
        "print (name.rstrip())\n",
        "print (name.strip())"
      ]
    }
  ]
}