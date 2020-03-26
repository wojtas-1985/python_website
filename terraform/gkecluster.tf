resource "google_container_cluster" "gke-cluster" {
  name               = "python-app"
  network            = "default"
  location           = "us-central1-c"
  initial_node_count = 1
  node_config 
  {
      preemptible  = false
      machine_type = "n1-standard-1"
      metadata =
       {
          disable-legacy-endpoints = "true"
       }
  }
}