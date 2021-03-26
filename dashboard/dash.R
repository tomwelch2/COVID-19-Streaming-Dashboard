library(aws.s3)
library(ggplot2)
library(dplyr)
library(shiny)
library(jsonlite)
library(viridis)
library(shinyWidgets)

#Connecting to S3 ---

source('/home/tom/Documents/projects/streaming/project3/dashboard/source.R')

Sys.setenv(
  "AWS_ACCESS_KEY_ID" = ACCESS_KEY,
  "AWS_SECRET_ACCESS_KEY" = SECRET_KEY,
  "AWS_DEFAULT_REGION" = REGION_NAME
)



ui <- fluidPage(
  setBackgroundColor("#f5f3f0"),
  titlePanel("COVID-19 Dashboard"),
  selectInput("regions", label = "Select a Region:",
               choices = c("Western Pacific Region",
                           "European Region",
                           "SouthEast Asia Region",
                           "Eastern Mediterranean Region",
                           "Region of the Americas",
                           "African Region"), width = 500),
  mainPanel(
    plotOutput("bar")
  )
)



server <- function(input, output){
  output$bar <- renderPlot({
    invalidateLater(1000)
      df <- s3read_using(read.csv, object = "s3://chartsbucket11/covid_kafka.csv")
      df$region <- as.character(df$region)
      new_df <- df %>% filter(region == input$regions)
    ggplot(new_df, aes(x = name, y = deaths, fill = deaths)) + geom_bar(stat = "identity") +
      ggtitle("COVID-19 Dashboard", subtitle = "Filtered By Region") +
      xlab(" ") + ylab("Deaths") + theme(
        axis.text.x = element_text(angle = 90, size = 13, hjust = 0.9),
        axis.text.y = element_text(size = 13),
        plot.title = element_text(size = 25),
        axis.title.y = element_text(size = 15),
        plot.subtitle = element_text(size = 15),
        legend.position = 'right',
        legend.key.height = unit(1, "cm"),
        panel.background = element_rect(fill = "white"),
        plot.background = element_rect(fill = "#ebe8e4"),
        legend.background = element_rect(fill = "#ebe8e4"),
        panel.grid.major = element_blank(),
        panel.grid.minor = element_line(colour = "black")
      ) + scale_fill_viridis(option = "C") + labs(fill = "Death Count")
    }, width = 1400, height = 500)
}


shinyApp(ui = ui, server = server)
