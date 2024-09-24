from pieces_os_client.api_client import ApiClient
from pieces_os_client.configuration import Configuration

class PiecesApiClient:
    def __init__(self, host):
        self.host = host
        self.api_client = ApiClient(Configuration(host))
        self._conversation_message_api = None
        self._conversation_messages_api = None
        self._conversations_api = None
        self._conversation_api = None
        self._qgpt_api = None
        self._user_api = None
        self._assets_api = None
        self._asset_api = None
        self._format_api = None
        self._connector_api = None
        self._models_api = None
        self._annotation_api = None
        self._annotations_api = None
        self._well_known_api = None
        self._os_api = None
        self._allocations_api = None
        self._linkfy_api = None
        self._search_api = None
        self._tag_api = None
        self._tags_api = None
        self._website_api = None
        self._websites_api = None

        # Websocket urls
        ws_base_url:str = host.replace('http','ws')
        self.ASSETS_IDENTIFIERS_WS_URL = ws_base_url + "/assets/stream/identifiers"
        self.AUTH_WS_URL = ws_base_url + "/user/stream"
        self.ASK_STREAM_WS_URL = ws_base_url + "/qgpt/stream"
        self.CONVERSATION_WS_URL = ws_base_url + "/conversations/stream/identifiers"
        self.HEALTH_WS_URL = ws_base_url + "/.well-known/stream/health"

    @property
    def conversation_message_api(self):
        if self._conversation_message_api is None:
            from pieces_os_client.api.conversation_message_api import ConversationMessageApi
            self._conversation_message_api = ConversationMessageApi(self.api_client)
        return self._conversation_message_api

    @property
    def conversation_messages_api(self):
        if self._conversation_messages_api is None:
            from pieces_os_client.api.conversation_messages_api import ConversationMessagesApi
            self._conversation_messages_api = ConversationMessagesApi(self.api_client)
        return self._conversation_messages_api

    @property
    def conversations_api(self):
        if self._conversations_api is None:
            from pieces_os_client.api.conversations_api import ConversationsApi
            self._conversations_api = ConversationsApi(self.api_client)
        return self._conversations_api

    @property
    def conversation_api(self):
        if self._conversation_api is None:
            from pieces_os_client.api.conversation_api import ConversationApi
            self._conversation_api = ConversationApi(self.api_client)
        return self._conversation_api

    @property
    def qgpt_api(self):
        if self._qgpt_api is None:
            from pieces_os_client.api.qgpt_api import QGPTApi
            self._qgpt_api = QGPTApi(self.api_client)
        return self._qgpt_api

    @property
    def user_api(self):
        if self._user_api is None:
            from pieces_os_client.api.user_api import UserApi
            self._user_api = UserApi(self.api_client)
        return self._user_api

    @property
    def assets_api(self):
        if self._assets_api is None:
            from pieces_os_client.api.assets_api import AssetsApi
            self._assets_api = AssetsApi(self.api_client)
        return self._assets_api

    @property
    def asset_api(self):
        if self._asset_api is None:
            from pieces_os_client.api.asset_api import AssetApi
            self._asset_api = AssetApi(self.api_client)
        return self._asset_api

    @property
    def format_api(self):
        if self._format_api is None:
            from pieces_os_client.api.format_api import FormatApi
            self._format_api = FormatApi(self.api_client)
        return self._format_api

    @property
    def connector_api(self):
        if self._connector_api is None:
            from pieces_os_client.api.connector_api import ConnectorApi
            self._connector_api = ConnectorApi(self.api_client)
        return self._connector_api

    @property
    def models_api(self):
        if self._models_api is None:
            from pieces_os_client.api.models_api import ModelsApi
            self._models_api = ModelsApi(self.api_client)
        return self._models_api

    @property
    def annotation_api(self):
        if self._annotation_api is None:
            from pieces_os_client.api.annotation_api import AnnotationApi
            self._annotation_api = AnnotationApi(self.api_client)
        return self._annotation_api

    @property
    def annotations_api(self):
        if self._annotations_api is None:
            from pieces_os_client.api.annotations_api import AnnotationsApi
            self._annotations_api = AnnotationsApi(self.api_client)
        return self._annotations_api

    @property
    def well_known_api(self):
        if self._well_known_api is None:
            from pieces_os_client.api.well_known_api import WellKnownApi
            self._well_known_api = WellKnownApi(self.api_client)
        return self._well_known_api

    @property
    def os_api(self):
        if self._os_api is None:
            from pieces_os_client.api.os_api import OSApi
            self._os_api = OSApi(self.api_client)
        return self._os_api

    @property
    def allocations_api(self):
        if self._allocations_api is None:
            from pieces_os_client.api.allocations_api import AllocationsApi
            self._allocations_api = AllocationsApi(self.api_client)
        return self._allocations_api

    @property
    def linkfy_api(self):
        if self._linkfy_api is None:
            from pieces_os_client.api.linkify_api import LinkifyApi
            self._linkfy_api = LinkifyApi(self.api_client)
        return self._linkfy_api

    @property
    def search_api(self):
        if self._search_api is None:
            from pieces_os_client.api.search_api import SearchApi
            self._search_api = SearchApi(self.api_client)
        return self._search_api

    @property
    def tag_api(self):
        if self._tag_api is None:
            from pieces_os_client.api.tag_api import TagApi
            self._tag_api = TagApi(self.api_client)
        return self._tag_api

    @property
    def tags_api(self):
        if self._tags_api is None:
            from pieces_os_client.api.tags_api import TagsApi
            self._tags_api = TagsApi(self.api_client)
        return self._tags_api

    @property
    def website_api(self):
        if self._website_api is None:
            from pieces_os_client.api.website_api import WebsiteApi
            self._website_api = WebsiteApi(self.api_client)
        return self._website_api

    @property
    def websites_api(self):
        if self._websites_api is None:
            from pieces_os_client.api.websites_api import WebsitesApi
            self._websites_api = WebsitesApi(self.api_client)
        return self._websites_api

