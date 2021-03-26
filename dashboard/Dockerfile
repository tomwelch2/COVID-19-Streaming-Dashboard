FROM rocker/tidyverse

ADD dash.R /

COPY ./source.R /source.R

RUN R -e "install.packages('aws.s3')"

RUN R -e "install.packages('ggplot2')"

RUN R -e "install.packages('dplyr')"

RUN R -e "install.packages('shiny')"

RUN R -e "install.packages('viridis')"

EXPOSE 3838

CMD R -e "shiny::runApp('dash.R', host = '0.0.0.0', port = 3838)"
