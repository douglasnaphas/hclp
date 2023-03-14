output "canary_output" {
  value = "something exists"
}

output "greeting" {
  value = format("%sOh, hello, %s, from %s.",
    var.greeting_prefix,
    var.greeting_to,
    var.greeting_from
  )
}
