variable "greeting_from" {
  description = "Who is the greeting from?"
  type = string
  default = "me"
}

variable "greeting_to" {
  description = "Who is the greeting to?"
  type = string
  default = "World"
}

variable "greeting_prefix" {
  description = "Something to say before the greeting"
  type = string
  default = ""
}