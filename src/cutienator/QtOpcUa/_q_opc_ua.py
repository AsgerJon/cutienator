"""
QOpcUa stands for the namespace 'QOpcUa' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.NamespaceGenerator from the records of Qt 6.12.0.
#  Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteFlags, CuteNum


class QOpcUa:
  """
  The namespace 'QOpcUa' of Qt, which holds no objects. It holds the 13 enums
  Qt writes in it, each under its name, and the 6 names Qt has for the
  combinations of a flags enum, each holding the class of that enum. It is
  never made into an object.
  """

  class AccessLevelBit(CuteFlags, number='unsigned char', scoped=True):
    """
    The flags enum 'QOpcUa::AccessLevelBit' of Qt, with the 8 names Qt gives
    in it. Qt names the type of its combinations 'QOpcUa::AccessLevel'. C++
    keeps these names inside the enum, so the class that holds the enum does
    not have them.
    """

    NULL = 0x0
    CurrentRead = 0x1
    CurrentWrite = 0x2
    HistoryRead = 0x4
    HistoryWrite = 0x8
    SemanticChange = 0x10
    StatusWrite = 0x20
    TimestampWrite = 0x40

  AccessLevel = AccessLevelBit

  class AccessLevelExBit(CuteFlags, number='unsigned int', scoped=True):
    """
    The flags enum 'QOpcUa::AccessLevelExBit' of Qt, with the 14 names Qt
    gives in it. Qt names the type of its combinations
    'QOpcUa::AccessLevelEx'. C++ keeps these names inside the enum, so the
    class that holds the enum does not have them.
    """

    NULL = 0x0
    CurrentRead = 0x1
    CurrentWrite = 0x2
    HistoryRead = 0x4
    HistoryWrite = 0x8
    SemanticChange = 0x10
    StatusWrite = 0x20
    TimestampWrite = 0x40
    NonatomicRead = 0x100
    NonatomicWrite = 0x200
    WriteFullArrayOnly = 0x400
    NoSubDataTypes = 0x800
    NonVolatile = 0x1000
    Constant = 0x2000

  AccessLevelEx = AccessLevelExBit

  class AxisScale(CuteNum, scoped=True):
    """
    The enum 'QOpcUa::AxisScale' of Qt, with the 3 names Qt gives in it. C++
    keeps these names inside the enum, so the class that holds the enum does
    not have them.
    """

    Linear = Kee[int](0)
    Log = Kee[int](1)
    Ln = Kee[int](2)

  class ErrorCategory(CuteNum, scoped=True):
    """
    The enum 'QOpcUa::ErrorCategory' of Qt, with the 8 names Qt gives in it.
    C++ keeps these names inside the enum, so the class that holds the enum
    does not have them.
    """

    NoError = Kee[int](0)
    NodeError = Kee[int](1)
    AttributeError = Kee[int](2)
    PermissionError = Kee[int](3)
    ArgumentError = Kee[int](4)
    TypeError = Kee[int](5)
    ConnectionError = Kee[int](6)
    UnspecifiedError = Kee[int](7)

  class EventNotifierBit(CuteFlags, number='unsigned char', scoped=True):
    """
    The flags enum 'QOpcUa::EventNotifierBit' of Qt, with the 4 names Qt
    gives in it. Qt names the type of its combinations
    'QOpcUa::EventNotifier'. C++ keeps these names inside the enum, so the
    class that holds the enum does not have them.
    """

    NULL = 0x0
    SubscribeToEvents = 0x1
    HistoryRead = 0x4
    HistoryWrite = 0x8

  EventNotifier = EventNotifierBit

  class IsAbstract(CuteNum, scoped=True):
    """
    The enum 'QOpcUa::IsAbstract' of Qt, with the 2 names Qt gives in it. C++
    keeps these names inside the enum, so the class that holds the enum does
    not have them.
    """

    NotAbstract = Kee[int](0)
    Abstract = Kee[int](1)

  class NodeAttribute(CuteFlags, scoped=True):
    """
    The flags enum 'QOpcUa::NodeAttribute' of Qt, with the 28 names Qt gives
    in it. Qt names the type of its combinations 'QOpcUa::NodeAttributes'.
    C++ keeps these names inside the enum, so the class that holds the enum
    does not have them.
    """

    NULL = 0x0
    NodeId = 0x1
    NodeClass = 0x2
    BrowseName = 0x4
    DisplayName = 0x8
    Description = 0x10
    WriteMask = 0x20
    UserWriteMask = 0x40
    IsAbstract = 0x80
    Symmetric = 0x100
    InverseName = 0x200
    ContainsNoLoops = 0x400
    EventNotifier = 0x800
    Value = 0x1000
    DataType = 0x2000
    ValueRank = 0x4000
    ArrayDimensions = 0x8000
    AccessLevel = 0x10000
    UserAccessLevel = 0x20000
    MinimumSamplingInterval = 0x40000
    Historizing = 0x80000
    Executable = 0x100000
    UserExecutable = 0x200000
    DataTypeDefinition = 0x400000
    RolePermissions = 0x800000
    UserRolePermissions = 0x1000000
    AccessRestrictions = 0x2000000
    AccessLevelEx = 0x4000000

  NodeAttributes = NodeAttribute

  class NodeClass(CuteFlags, scoped=True):
    """
    The flags enum 'QOpcUa::NodeClass' of Qt, with the 9 names Qt gives in
    it. Qt names the type of its combinations 'QOpcUa::NodeClasses'. C++
    keeps these names inside the enum, so the class that holds the enum does
    not have them.
    """

    Undefined = 0x0
    Object = 0x1
    Variable = 0x2
    Method = 0x4
    ObjectType = 0x8
    VariableType = 0x10
    ReferenceType = 0x20
    DataType = 0x40
    View = 0x80

  NodeClasses = NodeClass

  class ReferenceTypeId(CuteNum, scoped=True):
    """
    The enum 'QOpcUa::ReferenceTypeId' of Qt, with the 68 names Qt gives in
    it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    Unspecified = Kee[int](0)
    References = Kee[int](31)
    NonHierarchicalReferences = Kee[int](32)
    HierarchicalReferences = Kee[int](33)
    HasChild = Kee[int](34)
    Organizes = Kee[int](35)
    HasEventSource = Kee[int](36)
    HasModellingRule = Kee[int](37)
    HasEncoding = Kee[int](38)
    HasDescription = Kee[int](39)
    HasTypeDefinition = Kee[int](40)
    GeneratesEvent = Kee[int](41)
    Aggregates = Kee[int](44)
    HasSubtype = Kee[int](45)
    HasProperty = Kee[int](46)
    HasComponent = Kee[int](47)
    HasNotifier = Kee[int](48)
    HasOrderedComponent = Kee[int](49)
    FromState = Kee[int](51)
    ToState = Kee[int](52)
    HasCause = Kee[int](53)
    HasEffect = Kee[int](54)
    HasHistoricalConfiguration = Kee[int](56)
    HasSubStateMachine = Kee[int](117)
    HasArgumentDescription = Kee[int](129)
    HasOptionalInputArgumentDescription = Kee[int](131)
    AlwaysGeneratesEvent = Kee[int](3065)
    HasTrueSubState = Kee[int](9004)
    HasFalseSubState = Kee[int](9005)
    HasCondition = Kee[int](9006)
    HasPubSubConnection = Kee[int](14476)
    DataSetToWriter = Kee[int](14936)
    HasGuard = Kee[int](15112)
    HasDataSetWriter = Kee[int](15296)
    HasDataSetReader = Kee[int](15297)
    HasAlarmSuppressionGroup = Kee[int](16361)
    AlarmGroupMember = Kee[int](16362)
    HasEffectDisable = Kee[int](17276)
    HasDictionaryEntry = Kee[int](17597)
    HasInterface = Kee[int](17603)
    HasAddIn = Kee[int](17604)
    HasEffectEnable = Kee[int](17983)
    HasEffectSuppressed = Kee[int](17984)
    HasEffectUnsuppressed = Kee[int](17985)
    HasWriterGroup = Kee[int](18804)
    HasReaderGroup = Kee[int](18805)
    AliasFor = Kee[int](23469)
    IsDeprecated = Kee[int](23562)
    HasStructuredComponent = Kee[int](24136)
    AssociatedWith = Kee[int](24137)
    UsesPriorityMappingTable = Kee[int](25237)
    HasLowerLayerInterface = Kee[int](25238)
    IsExecutableOn = Kee[int](25253)
    Controls = Kee[int](25254)
    Utilizes = Kee[int](25255)
    Requires = Kee[int](25256)
    IsPhysicallyConnectedTo = Kee[int](25257)
    RepresentsSameEntityAs = Kee[int](25258)
    RepresentsSameHardwareAs = Kee[int](25259)
    RepresentsSameFunctionalityAs = Kee[int](25260)
    IsHostedBy = Kee[int](25261)
    HasPhysicalComponent = Kee[int](25262)
    HasContainedComponent = Kee[int](25263)
    HasAttachedComponent = Kee[int](25264)
    IsExecutingOn = Kee[int](25265)
    HasPushedSecurityGroup = Kee[int](25345)
    AlarmSuppressionGroupMember = Kee[int](32059)
    HasReferenceDescription = Kee[int](32679)

  class TimestampsToReturn(CuteNum, scoped=True):
    """
    The enum 'QOpcUa::TimestampsToReturn' of Qt, with the 5 names Qt gives in
    it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    Source = Kee[int](0)
    Server = Kee[int](1)
    Both = Kee[int](2)
    Neither = Kee[int](4)
    Invalid = Kee[int](5)

  class Types(CuteNum):
    """The enum 'QOpcUa::Types' of Qt, with the 42 names Qt gives in it."""

    Boolean = Kee[int](0)
    Int32 = Kee[int](1)
    UInt32 = Kee[int](2)
    Double = Kee[int](3)
    Float = Kee[int](4)
    String = Kee[int](5)
    LocalizedText = Kee[int](6)
    DateTime = Kee[int](7)
    UInt16 = Kee[int](8)
    Int16 = Kee[int](9)
    UInt64 = Kee[int](10)
    Int64 = Kee[int](11)
    Byte = Kee[int](12)
    SByte = Kee[int](13)
    ByteString = Kee[int](14)
    XmlElement = Kee[int](15)
    NodeId = Kee[int](16)
    Guid = Kee[int](17)
    QualifiedName = Kee[int](18)
    StatusCode = Kee[int](19)
    ExtensionObject = Kee[int](20)
    Range = Kee[int](21)
    EUInformation = Kee[int](22)
    ComplexNumber = Kee[int](23)
    DoubleComplexNumber = Kee[int](24)
    AxisInformation = Kee[int](25)
    XV = Kee[int](26)
    ExpandedNodeId = Kee[int](27)
    Argument = Kee[int](28)
    StructureDefinition = Kee[int](29)
    StructureField = Kee[int](30)
    EnumDefinition = Kee[int](31)
    EnumField = Kee[int](32)
    DiagnosticInfo = Kee[int](33)
    SimpleAttributeOperand = Kee[int](34)
    AttributeOperand = Kee[int](35)
    LiteralOperand = Kee[int](36)
    ElementOperand = Kee[int](37)
    RelativePathElement = Kee[int](38)
    ContentFilterElement = Kee[int](39)
    EventFilter = Kee[int](40)
    Undefined = Kee[int](4294967295)

  class UaStatusCode(CuteNum):
    """
    The enum 'QOpcUa::UaStatusCode' of Qt, with the 264 names Qt gives in it.
    """

    Good = Kee[int](0)
    Uncertain = Kee[int](1073741824)
    Bad = Kee[int](2147483648)
    BadUnexpectedError = Kee[int](2147549184)
    BadInternalError = Kee[int](2147614720)
    BadOutOfMemory = Kee[int](2147680256)
    BadResourceUnavailable = Kee[int](2147745792)
    BadCommunicationError = Kee[int](2147811328)
    BadEncodingError = Kee[int](2147876864)
    BadDecodingError = Kee[int](2147942400)
    BadEncodingLimitsExceeded = Kee[int](2148007936)
    BadRequestTooLarge = Kee[int](2159542272)
    BadResponseTooLarge = Kee[int](2159607808)
    BadUnknownResponse = Kee[int](2148073472)
    BadTimeout = Kee[int](2148139008)
    BadServiceUnsupported = Kee[int](2148204544)
    BadShutdown = Kee[int](2148270080)
    BadServerNotConnected = Kee[int](2148335616)
    BadServerHalted = Kee[int](2148401152)
    BadNothingToDo = Kee[int](2148466688)
    BadTooManyOperations = Kee[int](2148532224)
    BadTooManyMonitoredItems = Kee[int](2161836032)
    BadDataTypeIdUnknown = Kee[int](2148597760)
    BadCertificateInvalid = Kee[int](2148663296)
    BadSecurityChecksFailed = Kee[int](2148728832)
    BadCertificatePolicyCheckFailed = Kee[int](2165571584)
    BadCertificateTimeInvalid = Kee[int](2148794368)
    BadCertificateIssuerTimeInvalid = Kee[int](2148859904)
    BadCertificateHostNameInvalid = Kee[int](2148925440)
    BadCertificateUriInvalid = Kee[int](2148990976)
    BadCertificateUseNotAllowed = Kee[int](2149056512)
    BadCertificateIssuerUseNotAllowed = Kee[int](2149122048)
    BadCertificateUntrusted = Kee[int](2149187584)
    BadCertificateRevocationUnknown = Kee[int](2149253120)
    BadCertificateIssuerRevocationUnknown = Kee[int](2149318656)
    BadCertificateRevoked = Kee[int](2149384192)
    BadCertificateIssuerRevoked = Kee[int](2149449728)
    BadCertificateChainIncomplete = Kee[int](2165112832)
    BadUserAccessDenied = Kee[int](2149515264)
    BadIdentityTokenInvalid = Kee[int](2149580800)
    BadIdentityTokenRejected = Kee[int](2149646336)
    BadSecureChannelIdInvalid = Kee[int](2149711872)
    BadInvalidTimestamp = Kee[int](2149777408)
    BadNonceInvalid = Kee[int](2149842944)
    BadSessionIdInvalid = Kee[int](2149908480)
    BadSessionClosed = Kee[int](2149974016)
    BadSessionNotActivated = Kee[int](2150039552)
    BadSubscriptionIdInvalid = Kee[int](2150105088)
    BadRequestHeaderInvalid = Kee[int](2150236160)
    BadTimestampsToReturnInvalid = Kee[int](2150301696)
    BadRequestCancelledByClient = Kee[int](2150367232)
    BadTooManyArguments = Kee[int](2162491392)
    BadLicenseExpired = Kee[int](2165178368)
    BadLicenseLimitsExceeded = Kee[int](2165243904)
    BadLicenseNotAvailable = Kee[int](2165309440)
    GoodSubscriptionTransferred = Kee[int](2949120)
    GoodCompletesAsynchronously = Kee[int](3014656)
    GoodOverload = Kee[int](3080192)
    GoodClamped = Kee[int](3145728)
    BadNoCommunication = Kee[int](2150694912)
    BadWaitingForInitialData = Kee[int](2150760448)
    BadNodeIdInvalid = Kee[int](2150825984)
    BadNodeIdUnknown = Kee[int](2150891520)
    BadAttributeIdInvalid = Kee[int](2150957056)
    BadIndexRangeInvalid = Kee[int](2151022592)
    BadIndexRangeNoData = Kee[int](2151088128)
    BadDataEncodingInvalid = Kee[int](2151153664)
    BadDataEncodingUnsupported = Kee[int](2151219200)
    BadNotReadable = Kee[int](2151284736)
    BadNotWritable = Kee[int](2151350272)
    BadOutOfRange = Kee[int](2151415808)
    BadNotSupported = Kee[int](2151481344)
    BadNotFound = Kee[int](2151546880)
    BadObjectDeleted = Kee[int](2151612416)
    BadNotImplemented = Kee[int](2151677952)
    BadMonitoringModeInvalid = Kee[int](2151743488)
    BadMonitoredItemIdInvalid = Kee[int](2151809024)
    BadMonitoredItemFilterInvalid = Kee[int](2151874560)
    BadMonitoredItemFilterUnsupported = Kee[int](2151940096)
    BadFilterNotAllowed = Kee[int](2152005632)
    BadStructureMissing = Kee[int](2152071168)
    BadEventFilterInvalid = Kee[int](2152136704)
    BadContentFilterInvalid = Kee[int](2152202240)
    BadFilterOperatorInvalid = Kee[int](2160132096)
    BadFilterOperatorUnsupported = Kee[int](2160197632)
    BadFilterOperandCountMismatch = Kee[int](2160263168)
    BadFilterOperandInvalid = Kee[int](2152267776)
    BadFilterElementInvalid = Kee[int](2160328704)
    BadFilterLiteralInvalid = Kee[int](2160394240)
    BadContinuationPointInvalid = Kee[int](2152333312)
    BadNoContinuationPoints = Kee[int](2152398848)
    BadReferenceTypeIdInvalid = Kee[int](2152464384)
    BadBrowseDirectionInvalid = Kee[int](2152529920)
    BadNodeNotInView = Kee[int](2152595456)
    BadNumericOverflow = Kee[int](2165440512)
    BadServerUriInvalid = Kee[int](2152660992)
    BadServerNameMissing = Kee[int](2152726528)
    BadDiscoveryUrlMissing = Kee[int](2152792064)
    BadSempahoreFileMissing = Kee[int](2152857600)
    BadRequestTypeInvalid = Kee[int](2152923136)
    BadSecurityModeRejected = Kee[int](2152988672)
    BadSecurityPolicyRejected = Kee[int](2153054208)
    BadTooManySessions = Kee[int](2153119744)
    BadUserSignatureInvalid = Kee[int](2153185280)
    BadApplicationSignatureInvalid = Kee[int](2153250816)
    BadNoValidCertificates = Kee[int](2153316352)
    BadIdentityChangeNotSupported = Kee[int](2160459776)
    BadRequestCancelledByRequest = Kee[int](2153381888)
    BadParentNodeIdInvalid = Kee[int](2153447424)
    BadReferenceNotAllowed = Kee[int](2153512960)
    BadNodeIdRejected = Kee[int](2153578496)
    BadNodeIdExists = Kee[int](2153644032)
    BadNodeClassInvalid = Kee[int](2153709568)
    BadBrowseNameInvalid = Kee[int](2153775104)
    BadBrowseNameDuplicated = Kee[int](2153840640)
    BadNodeAttributesInvalid = Kee[int](2153906176)
    BadTypeDefinitionInvalid = Kee[int](2153971712)
    BadSourceNodeIdInvalid = Kee[int](2154037248)
    BadTargetNodeIdInvalid = Kee[int](2154102784)
    BadDuplicateReferenceNotAllowed = Kee[int](2154168320)
    BadInvalidSelfReference = Kee[int](2154233856)
    BadReferenceLocalOnly = Kee[int](2154299392)
    BadNoDeleteRights = Kee[int](2154364928)
    UncertainReferenceNotDeleted = Kee[int](1086062592)
    BadServerIndexInvalid = Kee[int](2154430464)
    BadViewIdUnknown = Kee[int](2154496000)
    BadViewTimestampInvalid = Kee[int](2160656384)
    BadViewParameterMismatch = Kee[int](2160721920)
    BadViewVersionInvalid = Kee[int](2160787456)
    UncertainNotAllNodesAvailable = Kee[int](1086324736)
    GoodResultsMayBeIncomplete = Kee[int](12189696)
    BadNotTypeDefinition = Kee[int](2160590848)
    UncertainReferenceOutOfServer = Kee[int](1080819712)
    BadTooManyMatches = Kee[int](2154627072)
    BadQueryTooComplex = Kee[int](2154692608)
    BadNoMatch = Kee[int](2154758144)
    BadMaxAgeInvalid = Kee[int](2154823680)
    BadSecurityModeInsufficient = Kee[int](2162556928)
    BadHistoryOperationInvalid = Kee[int](2154889216)
    BadHistoryOperationUnsupported = Kee[int](2154954752)
    BadInvalidTimestampArgument = Kee[int](2159869952)
    BadWriteNotSupported = Kee[int](2155020288)
    BadTypeMismatch = Kee[int](2155085824)
    BadMethodInvalid = Kee[int](2155151360)
    BadArgumentsMissing = Kee[int](2155216896)
    BadNotExecutable = Kee[int](2165374976)
    BadTooManySubscriptions = Kee[int](2155282432)
    BadTooManyPublishRequests = Kee[int](2155347968)
    BadNoSubscription = Kee[int](2155413504)
    BadSequenceNumberUnknown = Kee[int](2155479040)
    GoodRetransmissionQueueNotSupported = Kee[int](14614528)
    BadMessageNotAvailable = Kee[int](2155544576)
    BadInsufficientClientProfile = Kee[int](2155610112)
    BadStateNotActive = Kee[int](2160001024)
    BadAlreadyExists = Kee[int](2165637120)
    BadTcpServerTooBusy = Kee[int](2155675648)
    BadTcpMessageTypeInvalid = Kee[int](2155741184)
    BadTcpSecureChannelUnknown = Kee[int](2155806720)
    BadTcpMessageTooLarge = Kee[int](2155872256)
    BadTcpNotEnoughResources = Kee[int](2155937792)
    BadTcpInternalError = Kee[int](2156003328)
    BadTcpEndpointUrlInvalid = Kee[int](2156068864)
    BadRequestInterrupted = Kee[int](2156134400)
    BadRequestTimeout = Kee[int](2156199936)
    BadSecureChannelClosed = Kee[int](2156265472)
    BadSecureChannelTokenUnknown = Kee[int](2156331008)
    BadSequenceNumberInvalid = Kee[int](2156396544)
    BadProtocolVersionUnsupported = Kee[int](2159935488)
    BadConfigurationError = Kee[int](2156462080)
    BadNotConnected = Kee[int](2156527616)
    BadDeviceFailure = Kee[int](2156593152)
    BadSensorFailure = Kee[int](2156658688)
    BadOutOfService = Kee[int](2156724224)
    BadDeadbandFilterInvalid = Kee[int](2156789760)
    UncertainNoCommunicationLastUsableValue = Kee[int](1083113472)
    UncertainLastUsableValue = Kee[int](1083179008)
    UncertainSubstituteValue = Kee[int](1083244544)
    UncertainInitialValue = Kee[int](1083310080)
    UncertainSensorNotAccurate = Kee[int](1083375616)
    UncertainEngineeringUnitsExceeded = Kee[int](1083441152)
    UncertainSubNormal = Kee[int](1083506688)
    GoodLocalOverride = Kee[int](9830400)
    BadRefreshInProgress = Kee[int](2157379584)
    BadConditionAlreadyDisabled = Kee[int](2157445120)
    BadConditionAlreadyEnabled = Kee[int](2160852992)
    BadConditionDisabled = Kee[int](2157510656)
    BadEventIdUnknown = Kee[int](2157576192)
    BadEventNotAcknowledgeable = Kee[int](2159738880)
    BadDialogNotActive = Kee[int](2160918528)
    BadDialogResponseInvalid = Kee[int](2160984064)
    BadConditionBranchAlreadyAcked = Kee[int](2161049600)
    BadConditionBranchAlreadyConfirmed = Kee[int](2161115136)
    BadConditionAlreadyShelved = Kee[int](2161180672)
    BadConditionNotShelved = Kee[int](2161246208)
    BadShelvingTimeOutOfRange = Kee[int](2161311744)
    BadNoData = Kee[int](2157641728)
    BadBoundNotFound = Kee[int](2161573888)
    BadBoundNotSupported = Kee[int](2161639424)
    BadDataLost = Kee[int](2157772800)
    BadDataUnavailable = Kee[int](2157838336)
    BadEntryExists = Kee[int](2157903872)
    BadNoEntryExists = Kee[int](2157969408)
    BadTimestampNotSupported = Kee[int](2158034944)
    GoodEntryInserted = Kee[int](10616832)
    GoodEntryReplaced = Kee[int](10682368)
    UncertainDataSubNormal = Kee[int](1084489728)
    GoodNoData = Kee[int](10813440)
    GoodMoreData = Kee[int](10878976)
    BadAggregateListMismatch = Kee[int](2161377280)
    BadAggregateNotSupported = Kee[int](2161442816)
    BadAggregateInvalidInputs = Kee[int](2161508352)
    BadAggregateConfigurationRejected = Kee[int](2161770496)
    GoodDataIgnored = Kee[int](14221312)
    BadRequestNotAllowed = Kee[int](2162425856)
    BadRequestNotComplete = Kee[int](2165506048)
    BadTransactionPending = Kee[int](2162688000)
    BadTicketRequired = Kee[int](2166292480)
    BadTicketInvalid = Kee[int](2166358016)
    BadLocked = Kee[int](2162753536)
    GoodEdited = Kee[int](14417920)
    GoodPostActionFailed = Kee[int](14483456)
    UncertainDominantValueChanged = Kee[int](1088290816)
    GoodDependentValueChanged = Kee[int](14680064)
    BadDominantValueChanged = Kee[int](2162229248)
    UncertainDependentValueChanged = Kee[int](1088552960)
    BadDependentValueChanged = Kee[int](2162360320)
    GoodEdited_DependentValueChanged = Kee[int](18219008)
    GoodEdited_DominantValueChanged = Kee[int](18284544)
    GoodEdited_DominantValueChanged_DependentValueChanged = Kee[int](18350080)
    BadEdited_OutOfRange = Kee[int](2165899264)
    BadInitialValue_OutOfRange = Kee[int](2165964800)
    BadOutOfRange_DominantValueChanged = Kee[int](2166030336)
    BadEdited_OutOfRange_DominantValueChanged = Kee[int](2166095872)
    BadOutOfRange_DominantValueChanged_DependentValueChanged = Kee[int](
        2166161408)
    BadEdited_OutOfRange_DominantValueChanged_DependentValueChanged = Kee[int](
        2166226944)
    GoodCommunicationEvent = Kee[int](10944512)
    GoodShutdownEvent = Kee[int](11010048)
    GoodCallAgain = Kee[int](11075584)
    GoodNonCriticalTimeout = Kee[int](11141120)
    BadInvalidArgument = Kee[int](2158690304)
    BadConnectionRejected = Kee[int](2158755840)
    BadDisconnect = Kee[int](2158821376)
    BadConnectionClosed = Kee[int](2158886912)
    BadInvalidState = Kee[int](2158952448)
    BadEndOfStream = Kee[int](2159017984)
    BadNoDataAvailable = Kee[int](2159083520)
    BadWaitingForResponse = Kee[int](2159149056)
    BadOperationAbandoned = Kee[int](2159214592)
    BadExpectedStreamToBlock = Kee[int](2159280128)
    BadWouldBlock = Kee[int](2159345664)
    BadSyntaxError = Kee[int](2159411200)
    BadMaxConnectionsReached = Kee[int](2159476736)
    UncertainTransducerInManual = Kee[int](1107820544)
    UncertainSimulatedValue = Kee[int](1107886080)
    UncertainSensorCalibration = Kee[int](1107951616)
    UncertainConfigurationError = Kee[int](1108279296)
    GoodCascadeInitializationAcknowledged = Kee[int](67174400)
    GoodCascadeInitializationRequest = Kee[int](67239936)
    GoodCascadeNotInvited = Kee[int](67305472)
    GoodCascadeNotSelected = Kee[int](67371008)
    GoodFaultStateActive = Kee[int](67567616)
    GoodInitiateFaultState = Kee[int](67633152)
    GoodCascade = Kee[int](67698688)
    BadDataSetIdInvalid = Kee[int](2162622464)

  class WriteMaskBit(CuteFlags, number='unsigned int', scoped=True):
    """
    The flags enum 'QOpcUa::WriteMaskBit' of Qt, with the 27 names Qt gives
    in it. Qt names the type of its combinations 'QOpcUa::WriteMask'. C++
    keeps these names inside the enum, so the class that holds the enum does
    not have them.
    """

    NULL = 0x0
    AccessLevel = 0x1
    ArrayDimensions = 0x2
    BrowseName = 0x4
    ContainsNoLoops = 0x8
    DataType = 0x10
    Description = 0x20
    DisplayName = 0x40
    EventNotifier = 0x80
    Executable = 0x100
    Historizing = 0x200
    InverseName = 0x400
    IsAbstract = 0x800
    MinimumSamplingInterval = 0x1000
    NodeClass = 0x2000
    NodeId = 0x4000
    Symmetric = 0x8000
    UserAccessLevel = 0x10000
    UserExecutable = 0x20000
    UserWriteMask = 0x40000
    ValueRank = 0x80000
    WriteMask = 0x100000
    ValueForVariableType = 0x200000
    DataTypeDefinition = 0x400000
    RolePermissions = 0x800000
    AccessRestrictions = 0x1000000
    AccessLevelEx = 0x2000000

  WriteMask = WriteMaskBit
