data "aws_ami" "amazon_ec2" {
      most_recent = true

  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd/ubuntu-jammy-22.04-amd64-server-*"]
  }

  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }

  owners = ["099720109477"] # Canonical 
}

resource "aws_instance" "ec2" {
  for_each      = var.instances
  ami           = data.aws_ami.amazon_ec2.image_id
  instance_type = each.value.instance_type
  subnet_id = aws_subnet.subnets[each.value.subnet].id  #value.subnet-->subnet in values.auto in instance and will do loop back with each.value
  vpc_security_group_ids = [aws_security_group.sg.id]
  associate_public_ip_address = true
  key_name = "nginx"
  user_data = each.value.user_data

  tags = {
    Name = "${each.key}"
  }
}