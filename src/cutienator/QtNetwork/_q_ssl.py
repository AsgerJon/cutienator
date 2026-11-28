"""
QSsl stands for the namespace 'QSsl' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.NamespaceGenerator from the records of Qt 6.12.0.
#  Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteFlags, CuteNum


class QSsl:
  """
  The namespace 'QSsl' of Qt, which holds no objects. It holds the 10 enums
  Qt writes in it, each under its name, and the 1 names Qt has for the
  combinations of a flags enum, each holding the class of that enum. It is
  never made into an object.
  """

  class AlertLevel(CuteNum, scoped=True):
    """
    The enum 'QSsl::AlertLevel' of Qt, with the 3 names Qt gives in it. C++
    keeps these names inside the enum, so the class that holds the enum does
    not have them.
    """

    Warning = Kee[int](0)
    Fatal = Kee[int](1)
    Unknown = Kee[int](2)

  class AlertType(CuteNum, scoped=True):
    """
    The enum 'QSsl::AlertType' of Qt, with the 34 names Qt gives in it. C++
    keeps these names inside the enum, so the class that holds the enum does
    not have them.
    """

    CloseNotify = Kee[int](0)
    UnexpectedMessage = Kee[int](10)
    BadRecordMac = Kee[int](20)
    RecordOverflow = Kee[int](22)
    DecompressionFailure = Kee[int](30)
    HandshakeFailure = Kee[int](40)
    NoCertificate = Kee[int](41)
    BadCertificate = Kee[int](42)
    UnsupportedCertificate = Kee[int](43)
    CertificateRevoked = Kee[int](44)
    CertificateExpired = Kee[int](45)
    CertificateUnknown = Kee[int](46)
    IllegalParameter = Kee[int](47)
    UnknownCa = Kee[int](48)
    AccessDenied = Kee[int](49)
    DecodeError = Kee[int](50)
    DecryptError = Kee[int](51)
    ExportRestriction = Kee[int](60)
    ProtocolVersion = Kee[int](70)
    InsufficientSecurity = Kee[int](71)
    InternalError = Kee[int](80)
    InappropriateFallback = Kee[int](86)
    UserCancelled = Kee[int](90)
    NoRenegotiation = Kee[int](100)
    MissingExtension = Kee[int](109)
    UnsupportedExtension = Kee[int](110)
    CertificateUnobtainable = Kee[int](111)
    UnrecognizedName = Kee[int](112)
    BadCertificateStatusResponse = Kee[int](113)
    BadCertificateHashValue = Kee[int](114)
    UnknownPskIdentity = Kee[int](115)
    CertificateRequired = Kee[int](116)
    NoApplicationProtocol = Kee[int](120)
    UnknownAlertMessage = Kee[int](255)

  class AlternativeNameEntryType(CuteNum):
    """
    The enum 'QSsl::AlternativeNameEntryType' of Qt, with the 3 names Qt
    gives in it.
    """

    EmailEntry = Kee[int](0)
    DnsEntry = Kee[int](1)
    IpAddressEntry = Kee[int](2)

  class EncodingFormat(CuteNum):
    """
    The enum 'QSsl::EncodingFormat' of Qt, with the 2 names Qt gives in it.
    """

    Pem = Kee[int](0)
    Der = Kee[int](1)

  class ImplementedClass(CuteNum, scoped=True):
    """
    The enum 'QSsl::ImplementedClass' of Qt, with the 7 names Qt gives in it.
    C++ keeps these names inside the enum, so the class that holds the enum
    does not have them.
    """

    Key = Kee[int](0)
    Certificate = Kee[int](1)
    Socket = Kee[int](2)
    DiffieHellman = Kee[int](3)
    EllipticCurve = Kee[int](4)
    Dtls = Kee[int](5)
    DtlsCookie = Kee[int](6)

  class KeyAlgorithm(CuteNum):
    """
    The enum 'QSsl::KeyAlgorithm' of Qt, with the 6 names Qt gives in it.
    """

    Opaque = Kee[int](0)
    Rsa = Kee[int](1)
    Dsa = Kee[int](2)
    Ec = Kee[int](3)
    Dh = Kee[int](4)
    MlDsa = Kee[int](5)

  class KeyType(CuteNum):
    """The enum 'QSsl::KeyType' of Qt, with the 2 names Qt gives in it."""

    PrivateKey = Kee[int](0)
    PublicKey = Kee[int](1)

  class SslOption(CuteFlags):
    """
    The flags enum 'QSsl::SslOption' of Qt, with the 8 names Qt gives in it.
    Qt names the type of its combinations 'QSsl::SslOptions'.
    """

    SslOptionDisableEmptyFragments = 0x1
    SslOptionDisableSessionTickets = 0x2
    SslOptionDisableCompression = 0x4
    SslOptionDisableServerNameIndication = 0x8
    SslOptionDisableLegacyRenegotiation = 0x10
    SslOptionDisableSessionSharing = 0x20
    SslOptionDisableSessionPersistence = 0x40
    SslOptionDisableServerCipherPreference = 0x80

  SslOptions = SslOption

  class SslProtocol(CuteNum):
    """
    The enum 'QSsl::SslProtocol' of Qt, with the 15 names Qt gives in it.
    """

    TlsV1_0 = Kee[int](0)
    TlsV1_1 = Kee[int](1)
    TlsV1_2 = Kee[int](2)
    AnyProtocol = Kee[int](3)
    SecureProtocols = Kee[int](4)
    TlsV1_0OrLater = Kee[int](5)
    TlsV1_1OrLater = Kee[int](6)
    TlsV1_2OrLater = Kee[int](7)
    DtlsV1_0 = Kee[int](8)
    DtlsV1_0OrLater = Kee[int](9)
    DtlsV1_2 = Kee[int](10)
    DtlsV1_2OrLater = Kee[int](11)
    TlsV1_3 = Kee[int](12)
    TlsV1_3OrLater = Kee[int](13)
    UnknownProtocol = Kee[int](-1)

  class SupportedFeature(CuteNum, scoped=True):
    """
    The enum 'QSsl::SupportedFeature' of Qt, with the 7 names Qt gives in it.
    C++ keeps these names inside the enum, so the class that holds the enum
    does not have them.
    """

    CertificateVerification = Kee[int](0)
    ClientSideAlpn = Kee[int](1)
    ServerSideAlpn = Kee[int](2)
    Ocsp = Kee[int](3)
    Psk = Kee[int](4)
    SessionTicket = Kee[int](5)
    Alerts = Kee[int](6)
