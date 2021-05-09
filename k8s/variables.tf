provider "azurerm" {
    features {}
}

variable "resource_grp" {
  type              = string  
  description       = "rg"
  default           = "aks"
}

variable "location" {
  type              = string  
  description       = "location of rg"
  default           = "eastus"
}

variable "resource_prefix" {
  type        = string
  description = "prefix"
  default     = "aks"
}

variable "vm_size" {
  type        = string
  description = "vm size"
  default     = "Standard_B2s"
}

variable "ssh_public_key" {
    default = "~/.ssh/id_rsa.pub"
}
