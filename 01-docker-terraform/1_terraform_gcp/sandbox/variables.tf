variable "credentials" {
  description = "My Credentials"
  default = "./keys/my-creds.json"
  
}
variable "project" {
  description = "Project Name"
  default = "terraform-demo-412422"
}
variable "bq_dataset_name" {
  description = "My BigQuery Dataset Name"
  default = "demo_dataset"
}
variable "region" {
  description = "Region"
  default = "me-west1-a"
}
variable "location" {
  description = "Project Location"
  default = "EU"
}
variable "gcs_storage_name" {
  description = "Bucket Storage Name"
  default = "terraform-demo-412422-terra-bucket"
}
variable "gcs_storage_class" {
  description = "Bucket Storage Class"
  default = "STANDARD"
}