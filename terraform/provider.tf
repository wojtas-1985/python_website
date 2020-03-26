provider "google" {
    credentials = file("./creds/serviceaccount.json")
    project     = "python-app-demo"
    region      = "us-central1-c"
}