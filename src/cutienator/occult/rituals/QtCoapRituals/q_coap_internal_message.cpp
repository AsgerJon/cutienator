//  Written by dev_tooling.RitualGenerator from the records of
//  QtCoap/6.12.0/QtCoap/private/qcoapinternalmessage_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-26: moc's output for 'QCoapInternalMessage' is
//  pasted in, cut from what the moc of Qt 6.12.0 writes for its header: Qt's
//  library keeps it to itself; added are 4 rituals that lean on what moc
//  writes for a class of the part Qt keeps to itself, whose ritual file
//  carries moc's output, drafted by a copy of the generator that lets those
//  names through. A copy of a meta-object is a second one: 'qobject_cast'
//  between it and Qt's own does not match. Kept as it is when the generator
//  runs again.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCoap/QtCoap>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCoap/6.12.0/QtCoap/private/qcoapinternalmessage_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCoap/qcoapmessage.h>
#include <QtCore/qbytearray.h>
#include <QtCoap/qcoapoption.h>
#include <QtCore/qurl.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qtmochelpers.h>
#include <memory>
#include <QtCore/qxptype_traits.h>
#include <QtCoap/private/qcoapinternalmessage_p.h>
#include <QtCoap/private/qcoaprequest_p.h>
#include <QtCoap/qcoaprequest.h>
#include <QtCore/qloggingcategory.h>
#include <QtCoap/private/qcoaprequest_p.h>
#include <QtCore/qmath.h>
#include <QtCore/qdatetime.h>
#include <QtCore/qloggingcategory.h>
#include <QtCore/QDebug>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from ../qtcoap/src/coap/qcoaprequest.cpp, line 18, as local:qcoaprequest.cpp:CoapScheme
namespace {
const auto CoapScheme = QLatin1String("coap");
}  // namespace

//  from ../qtcoap/src/coap/qcoaprequest.cpp, line 19, as local:qcoaprequest.cpp:CoapSecureScheme
namespace {
const auto CoapSecureScheme = QLatin1String("coaps");
}  // namespace

//  from QtCoap__QCoapInternalMessage.cpp, line 1, as moc:QCoapInternalMessage
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN20QCoapInternalMessageE_t {};
} // unnamed namespace

template <> constexpr inline auto QCoapInternalMessage::qt_create_metaobjectdata<qt_meta_tag_ZN20QCoapInternalMessageE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "QCoapInternalMessage"
    };

    QtMocHelpers::UintData qt_methods {
    };
    QtMocHelpers::UintData qt_properties {
    };
    QtMocHelpers::UintData qt_enums {
    };
    return QtMocHelpers::metaObjectData<QCoapInternalMessage, qt_meta_tag_ZN20QCoapInternalMessageE_t>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums);
}
Q_CONSTINIT const QMetaObject QCoapInternalMessage::staticMetaObject = { {
    QMetaObject::SuperData::link<QObject::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN20QCoapInternalMessageE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN20QCoapInternalMessageE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN20QCoapInternalMessageE_t>.metaTypes,
    nullptr
} };

void QCoapInternalMessage::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<QCoapInternalMessage *>(_o);
    (void)_t;
    (void)_c;
    (void)_id;
    (void)_a;
}

const QMetaObject *QCoapInternalMessage::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QCoapInternalMessage::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN20QCoapInternalMessageE_t>.strings))
        return static_cast<void*>(this);
    return QObject::qt_metacast(_clname);
}

int QCoapInternalMessage::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QObject::qt_metacall(_c, _id, _a);
    return _id;
}
QT_WARNING_POP

//  from ../qtcoap/src/coap/qcoapinternalmessage.cpp, line 141, as _ZN20QCoapInternalMessage9addOptionERK11QCoapOption
inline void QCoapInternalMessage::addOption(const QCoapOption &option)
{
    Q_D(QCoapInternalMessage);
    d->message.addOption(option);
}

//  from ../qtcoap/src/coap/qcoapinternalmessage.cpp, line 220, as _ZNK20QCoapInternalMessage7isValidEv
inline bool QCoapInternalMessage::isValid() const
{
    return true;
}

//  from ../qtcoap/src/coap/qcoapinternalmessage.cpp, line 21, as _ZN27QCoapInternalMessagePrivateD1Ev
inline QCoapInternalMessagePrivate::~QCoapInternalMessagePrivate()
{
}

//  from ../qtcoap/src/coap/qcoaprequest.cpp, line 236, as _ZN19QCoapRequestPrivate10isUrlValidERK4QUrl
inline bool QCoapRequestPrivate::isUrlValid(const QUrl &url)
{
    return (url.isValid() && !url.isLocalFile() && !url.isRelative()
            && (url.scheme() == CoapScheme || url.scheme() == CoapSecureScheme)
            && !url.hasFragment());
}

//  from ../qtcoap/src/coap/qcoapinternalmessage.cpp, line 14, as _Z14lcCoapExchangev
inline const QLoggingCategory &lcCoapExchange()
{
    static const QLoggingCategory category("qt.coap.exchange");
    return category;
}

//  from ../qtcoap/src/coap/qcoapinternalmessage.cpp, line 48, as _ZN20QCoapInternalMessageC1EP7QObject
inline QCoapInternalMessage::QCoapInternalMessage(QObject *parent) :
    QObject(*new QCoapInternalMessagePrivate, parent)
{
}

//  from ../qtcoap/src/coap/qcoapinternalmessage.cpp, line 59, as _ZN20QCoapInternalMessageC1ERK12QCoapMessageP7QObject
inline QCoapInternalMessage::QCoapInternalMessage(const QCoapMessage &message, QObject *parent) :
    QCoapInternalMessage(parent)
{
    Q_D(QCoapInternalMessage);
    d->message = message;
}

//  from ../qtcoap/src/coap/qcoapinternalmessage.cpp, line 118, as _ZN20QCoapInternalMessage9addOptionEN11QCoapOption10OptionNameERK10QByteArray
inline void QCoapInternalMessage::addOption(QCoapOption::OptionName name, const QByteArray &value)
{
    QCoapOption option(name, value);
    addOption(option);
}

//  from ../qtcoap/src/coap/qcoapinternalmessage.cpp, line 130, as _ZN20QCoapInternalMessage9addOptionEN11QCoapOption10OptionNameEj
inline void QCoapInternalMessage::addOption(QCoapOption::OptionName name, quint32 value)
{
    QCoapOption option(name, value);
    addOption(option);
}

//  from ../qtcoap/src/coap/qcoapinternalmessage.cpp, line 152, as _ZN20QCoapInternalMessage12removeOptionEN11QCoapOption10OptionNameE
inline void QCoapInternalMessage::removeOption(QCoapOption::OptionName name)
{
    Q_D(QCoapInternalMessage);
    d->message.removeOption(name);
}

//  from ../qtcoap/src/coap/qcoapinternalmessage.cpp, line 163, as _ZN20QCoapInternalMessage7messageEv
inline QCoapMessage *QCoapInternalMessage::message()
{
    Q_D(QCoapInternalMessage);
    return &(d->message);
}

//  from ../qtcoap/src/coap/qcoapinternalmessage.cpp, line 174, as _ZNK20QCoapInternalMessage7messageEv
inline const QCoapMessage *QCoapInternalMessage::message() const
{
    Q_D(const QCoapInternalMessage);
    return &(d->message);
}

//  from ../qtcoap/src/coap/qcoapinternalmessage.cpp, line 185, as _ZNK20QCoapInternalMessage18currentBlockNumberEv
inline uint QCoapInternalMessage::currentBlockNumber() const
{
    Q_D(const QCoapInternalMessage);
    return d->currentBlockNumber;
}

//  from ../qtcoap/src/coap/qcoapinternalmessage.cpp, line 196, as _ZNK20QCoapInternalMessage22hasMoreBlocksToReceiveEv
inline bool QCoapInternalMessage::hasMoreBlocksToReceive() const
{
    Q_D(const QCoapInternalMessage);
    return d->hasNextBlock;
}

//  from ../qtcoap/src/coap/qcoapinternalmessage.cpp, line 207, as _ZNK20QCoapInternalMessage9blockSizeEv
inline uint QCoapInternalMessage::blockSize() const
{
    Q_D(const QCoapInternalMessage);
    return d->blockSize;
}

//  from ../qtcoap/src/coap/qcoapinternalmessage.cpp, line 232, as _ZN20QCoapInternalMessage10isUrlValidERK4QUrl
inline bool QCoapInternalMessage::isUrlValid(const QUrl &url)
{
    return QCoapRequestPrivate::isUrlValid(url);
}

//  from ../qtcoap/src/coap/qcoapinternalmessage.cpp, line 72, as _ZN20QCoapInternalMessageC1ER27QCoapInternalMessagePrivateP7QObject
inline QCoapInternalMessage::QCoapInternalMessage(QCoapInternalMessagePrivate &dd, QObject *parent):
    QObject(dd, parent)
{
}

//  from ../qtcoap/src/coap/qcoapinternalmessage.cpp, line 87, as _ZN20QCoapInternalMessage29setFromDescriptiveBlockOptionERK11QCoapOption
inline void QCoapInternalMessage::setFromDescriptiveBlockOption(const QCoapOption &option)
{
    Q_D(QCoapInternalMessage);

    const auto value = option.opaqueValue();
    const quint8 *optionData = reinterpret_cast<const quint8 *>(value.data());

    // A zero-length block option is valid and encodes NUM=0, M=0, SZX=0
    // (RFC 7959 §2.2). Treat the absent last byte as 0 instead of reading
    // optionData[-1]; the loop below is then skipped and every field resolves to 0.
    const quint8 lastByte = option.length() > 0 ? optionData[option.length() - 1] : 0;
    quint32 blockNumber = 0;

    for (int i = 0; i < option.length() - 1; ++i)
        blockNumber = (blockNumber << 8) | optionData[i];

    blockNumber = (blockNumber << 4) | (lastByte >> 4);
    d->currentBlockNumber = blockNumber;
    d->hasNextBlock = ((lastByte & 0x8) == 0x8);
    d->blockSize = static_cast<uint>(1u << ((lastByte & 0x7) + 4));

    if (d->blockSize > 1024)
        qCWarning(lcCoapExchange, "Received a block size larger than 1024, something may be wrong.");
}
//  -----------------------------------------------------------------------

//  A QCoapInternalMessage that Python can take functions over in. Every QCoapInternalMessage
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQCoapInternalMessageCall0)(const void *, const QCoapOption *, int *);
typedef bool (*CuteQCoapInternalMessageCall1)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQCoapInternalMessageCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQCoapInternalMessageCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCoapInternalMessageCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCoapInternalMessageCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCoapInternalMessageCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCoapInternalMessageCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCoapInternalMessageCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQCoapInternalMessage : public QCoapInternalMessage {
public:
  using QCoapInternalMessage::QCoapInternalMessage;
  void *taken[9] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN20QCoapInternalMessage9addOptionERK11QCoapOption")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20QCoapInternalMessage7isValidEv")) {
      taken[1] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void QCoapInternalMessage::addOption(const QCoapOption &option)
  void addOption(const QCoapOption &option) override {
    if (taken[0]) {
      int handled = 0;
      CuteQCoapInternalMessageCall0 call = reinterpret_cast<CuteQCoapInternalMessageCall0>(taken[0]);
      call(this, &option, &handled);
      if (handled) return;
    }
    QCoapInternalMessage::addOption(option);
  }

  //  bool QCoapInternalMessage::isValid() const
  bool isValid() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQCoapInternalMessageCall1 call = reinterpret_cast<CuteQCoapInternalMessageCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QCoapInternalMessage::isValid();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQCoapInternalMessageCall2 call = reinterpret_cast<CuteQCoapInternalMessageCall2>(taken[2]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQCoapInternalMessageCall3 call = reinterpret_cast<CuteQCoapInternalMessageCall3>(taken[3]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQCoapInternalMessageCall4 call = reinterpret_cast<CuteQCoapInternalMessageCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQCoapInternalMessageCall5 call = reinterpret_cast<CuteQCoapInternalMessageCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQCoapInternalMessageCall6 call = reinterpret_cast<CuteQCoapInternalMessageCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[7]) {
      int handled = 0;
      CuteQCoapInternalMessageCall7 call = reinterpret_cast<CuteQCoapInternalMessageCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[8]) {
      int handled = 0;
      CuteQCoapInternalMessageCall8 call = reinterpret_cast<CuteQCoapInternalMessageCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QCoapInternalMessage::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK20QCoapInternalMessage10metaObjectEv(
    const QCoapInternalMessage *self) {
  return self->metaObject();
}

//  void *QCoapInternalMessage::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN20QCoapInternalMessage11qt_metacastEPKc(
    QCoapInternalMessage *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QCoapInternalMessage::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN20QCoapInternalMessage11qt_metacallEN11QMetaObject4CallEiPPv(
    QCoapInternalMessage *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QCoapInternalMessage::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN20QCoapInternalMessage2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QCoapInternalMessage::tr(s, c, n));
}

//  QCoapInternalMessage::QCoapInternalMessage(QObject *parent)
extern "C" Q_DECL_EXPORT
QCoapInternalMessage *ritual_ZN20QCoapInternalMessageC1EP7QObject(
    QObject *parent) {
  return new CuteQCoapInternalMessage(parent);
}

//  QCoapInternalMessage::QCoapInternalMessage(const QCoapMessage &message,
//      QObject *parent)
extern "C" Q_DECL_EXPORT
QCoapInternalMessage *ritual_ZN20QCoapInternalMessageC1ERK12QCoapMessageP7QObject(
    const QCoapMessage *message,
    QObject *parent) {
  return new CuteQCoapInternalMessage(*message, parent);
}

//  QCoapInternalMessage::~QCoapInternalMessage()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QCoapInternalMessageD1Ev(QCoapInternalMessage *self) {
  delete self;
}

//  void QCoapInternalMessage::addOption(QCoapOption::OptionName name, const
//      QByteArray &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QCoapInternalMessage9addOptionEN11QCoapOption10OptionNameERK10QByteArray(
    QCoapInternalMessage *self,
    QCoapOption::OptionName name,
    const QByteArray *value) {
  self->addOption(name, *value);
}

//  void QCoapInternalMessage::addOption(QCoapOption::OptionName name,
//      quint32 value)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QCoapInternalMessage9addOptionEN11QCoapOption10OptionNameEj(
    QCoapInternalMessage *self,
    QCoapOption::OptionName name,
    quint32 value) {
  self->addOption(name, value);
}

//  void QCoapInternalMessage::addOption(const QCoapOption &option)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QCoapInternalMessage9addOptionERK11QCoapOption(
    QCoapInternalMessage *self,
    const QCoapOption *option) {
  self->addOption(*option);
}

//  void QCoapInternalMessage::removeOption(QCoapOption::OptionName name)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QCoapInternalMessage12removeOptionEN11QCoapOption10OptionNameE(
    QCoapInternalMessage *self,
    QCoapOption::OptionName name) {
  self->removeOption(name);
}

//  QCoapMessage *QCoapInternalMessage::message()
extern "C" Q_DECL_EXPORT
QCoapMessage *ritual_ZN20QCoapInternalMessage7messageEv(
    QCoapInternalMessage *self) {
  return self->message();
}

//  const QCoapMessage *QCoapInternalMessage::message() const
extern "C" Q_DECL_EXPORT
const QCoapMessage *ritual_ZNK20QCoapInternalMessage7messageEv(
    const QCoapInternalMessage *self) {
  return self->message();
}

//  uint QCoapInternalMessage::currentBlockNumber() const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK20QCoapInternalMessage18currentBlockNumberEv(
    const QCoapInternalMessage *self) {
  return self->currentBlockNumber();
}

//  bool QCoapInternalMessage::hasMoreBlocksToReceive() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QCoapInternalMessage22hasMoreBlocksToReceiveEv(
    const QCoapInternalMessage *self) {
  return self->hasMoreBlocksToReceive();
}

//  uint QCoapInternalMessage::blockSize() const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK20QCoapInternalMessage9blockSizeEv(
    const QCoapInternalMessage *self) {
  return self->blockSize();
}

//  bool QCoapInternalMessage::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QCoapInternalMessage7isValidEv(
    const QCoapInternalMessage *self) {
  return self->isValid();
}

//  bool QCoapInternalMessage::isUrlValid(const QUrl &url)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QCoapInternalMessage10isUrlValidERK4QUrl(const QUrl *url) {
  return QCoapInternalMessage::isUrlValid(*url);
}

//  QCoapInternalMessage::QCoapInternalMessage(QCoapInternalMessagePrivate
//      &dd, QObject *parent)
extern "C" Q_DECL_EXPORT
QCoapInternalMessage *ritual_ZN20QCoapInternalMessageC1ER27QCoapInternalMessagePrivateP7QObject(
    QCoapInternalMessagePrivate *dd,
    QObject *parent) {
  return new CuteQCoapInternalMessage(*dd, parent);
}

//  void QCoapInternalMessage::setFromDescriptiveBlockOption(const
//      QCoapOption &option)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QCoapInternalMessage29setFromDescriptiveBlockOptionERK11QCoapOption(
    QCoapInternalMessage *self,
    const QCoapOption *option) {
  self->setFromDescriptiveBlockOption(*option);
}

//  QCoapInternalMessagePrivate *QCoapInternalMessage::d_func()
extern "C" Q_DECL_EXPORT
QCoapInternalMessagePrivate *ritual_ZN20QCoapInternalMessage6d_funcEv(
    QCoapInternalMessage *self) {
  return self->d_func();
}

//  const QCoapInternalMessagePrivate *QCoapInternalMessage::d_func() const
extern "C" Q_DECL_EXPORT
const QCoapInternalMessagePrivate *ritual_ZNK20QCoapInternalMessage6d_funcEv(
    const QCoapInternalMessage *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQCoapInternalMessage, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QCoapInternalMessage(
    QCoapInternalMessage *self,
    const char *key,
    void *call) {
  return static_cast<CuteQCoapInternalMessage *>(self)->take(key, call);
}

//  void QCoapInternalMessage::addOption(const QCoapOption &option)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QCoapInternalMessage9addOptionERK11QCoapOption(
    QCoapInternalMessage *self,
    const QCoapOption *option) {
  self->QCoapInternalMessage::addOption(*option);
}

//  bool QCoapInternalMessage::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK20QCoapInternalMessage7isValidEv(
    const QCoapInternalMessage *self) {
  return self->QCoapInternalMessage::isValid();
}
