# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
class ListMediaWorkflowExecutionsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Mts', '2014-06-18', 'ListMediaWorkflowExecutions')

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_MediaWorkflowId(self):
		return self.get_query_params().get('MediaWorkflowId')

	def set_MediaWorkflowId(self,MediaWorkflowId):
		self.add_query_param('MediaWorkflowId',MediaWorkflowId)

	def get_MediaWorkflowName(self):
		return self.get_query_params().get('MediaWorkflowName')

	def set_MediaWorkflowName(self,MediaWorkflowName):
		self.add_query_param('MediaWorkflowName',MediaWorkflowName)

	def get_InputFileURL(self):
		return self.get_query_params().get('InputFileURL')

	def set_InputFileURL(self,InputFileURL):
		self.add_query_param('InputFileURL',InputFileURL)

	def get_NextPageToken(self):
		return self.get_query_params().get('NextPageToken')

	def set_NextPageToken(self,NextPageToken):
		self.add_query_param('NextPageToken',NextPageToken)

	def get_MaximumPageSize(self):
		return self.get_query_params().get('MaximumPageSize')

	def set_MaximumPageSize(self,MaximumPageSize):
		self.add_query_param('MaximumPageSize',MaximumPageSize)

	def get_OwnerAccount(self):
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self,OwnerAccount):
		self.add_query_param('OwnerAccount',OwnerAccount)