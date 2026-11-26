//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpcUa/qopcuanode.h, Qt 6.12.0. Changes made here are lost.
#include <QtOpcUa/qopcuanode.h>
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qdatetime.h>
#include <QtOpcUa/qopcuamonitoringparameters.h>
#include <QtOpcUa/qopcuarelativepathelement.h>
#include <QtOpcUa/qopcuabrowserequest.h>
#include <QtOpcUa/qopcuareferencedescription.h>
#include <QtOpcUa/qopcuabrowsepathtarget.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QOpcUaNode that Python can take functions over in. Every QOpcUaNode
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQOpcUaNodeCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQOpcUaNodeCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQOpcUaNodeCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQOpcUaNodeCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQOpcUaNodeCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQOpcUaNodeCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQOpcUaNodeCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQOpcUaNode : public QOpcUaNode {
public:
  using QOpcUaNode::QOpcUaNode;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQOpcUaNodeCall0 call = reinterpret_cast<CuteQOpcUaNodeCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQOpcUaNodeCall1 call = reinterpret_cast<CuteQOpcUaNodeCall1>(taken[1]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQOpcUaNodeCall2 call = reinterpret_cast<CuteQOpcUaNodeCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQOpcUaNodeCall3 call = reinterpret_cast<CuteQOpcUaNodeCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQOpcUaNodeCall4 call = reinterpret_cast<CuteQOpcUaNodeCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[5]) {
      int handled = 0;
      CuteQOpcUaNodeCall5 call = reinterpret_cast<CuteQOpcUaNodeCall5>(taken[5]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQOpcUaNodeCall6 call = reinterpret_cast<CuteQOpcUaNodeCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QOpcUaNode::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10QOpcUaNode10metaObjectEv(
    const QOpcUaNode *self) {
  return self->metaObject();
}

//  void *QOpcUaNode::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10QOpcUaNode11qt_metacastEPKc(
    QOpcUaNode *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QOpcUaNode::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10QOpcUaNode11qt_metacallEN11QMetaObject4CallEiPPv(
    QOpcUaNode *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QOpcUaNode::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10QOpcUaNode2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QOpcUaNode::tr(s, c, n));
}

//  QOpcUaNodePrivate *QOpcUaNode::d_func()
extern "C" Q_DECL_EXPORT
QOpcUaNodePrivate *ritual_ZN10QOpcUaNode6d_funcEv(QOpcUaNode *self) {
  return self->d_func();
}

//  const QOpcUaNodePrivate *QOpcUaNode::d_func() const
extern "C" Q_DECL_EXPORT
const QOpcUaNodePrivate *ritual_ZNK10QOpcUaNode6d_funcEv(
    const QOpcUaNode *self) {
  return self->d_func();
}

//  QOpcUa::NodeAttributes QOpcUaNode::mandatoryBaseAttributes()
extern "C" Q_DECL_EXPORT
int ritual_ZN10QOpcUaNode23mandatoryBaseAttributesEv() {
  return static_cast<int>(QOpcUaNode::mandatoryBaseAttributes().toInt());
}

//  QOpcUa::NodeAttributes QOpcUaNode::allBaseAttributes()
extern "C" Q_DECL_EXPORT
int ritual_ZN10QOpcUaNode17allBaseAttributesEv() {
  return static_cast<int>(QOpcUaNode::allBaseAttributes().toInt());
}

//  QOpcUaNode::QOpcUaNode(QOpcUaNodeImpl *impl, QOpcUaClient *client,
//      QObject *parent)
extern "C" Q_DECL_EXPORT
QOpcUaNode *ritual_ZN10QOpcUaNodeC1EP14QOpcUaNodeImplP12QOpcUaClientP7QObject(
    QOpcUaNodeImpl *impl,
    QOpcUaClient *client,
    QObject *parent) {
  return new CuteQOpcUaNode(impl, client, parent);
}

//  QOpcUaNode::~QOpcUaNode()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QOpcUaNodeD1Ev(QOpcUaNode *self) {
  delete self;
}

//  bool QOpcUaNode::readAttributes(QOpcUa::NodeAttributes attributes)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QOpcUaNode14readAttributesE6QFlagsIN6QOpcUa13NodeAttributeEE(
    QOpcUaNode *self,
    int attributes) {
  return self->readAttributes(
      QFlags<QOpcUa::NodeAttribute>::fromInt(attributes));
}

//  bool QOpcUaNode::readAttributeRange(QOpcUa::NodeAttribute attribute,
//      const QString &indexRange)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QOpcUaNode18readAttributeRangeEN6QOpcUa13NodeAttributeERK7QString(
    QOpcUaNode *self,
    QOpcUa::NodeAttribute attribute,
    const QString *indexRange) {
  return self->readAttributeRange(attribute, *indexRange);
}

//  bool QOpcUaNode::readValueAttribute()
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QOpcUaNode18readValueAttributeEv(QOpcUaNode *self) {
  return self->readValueAttribute();
}

//  QVariant QOpcUaNode::attribute(QOpcUa::NodeAttribute attribute) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK10QOpcUaNode9attributeEN6QOpcUa13NodeAttributeE(
    const QOpcUaNode *self,
    QOpcUa::NodeAttribute attribute) {
  return new QVariant(self->attribute(attribute));
}

//  QVariant QOpcUaNode::valueAttribute() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK10QOpcUaNode14valueAttributeEv(const QOpcUaNode *self) {
  return new QVariant(self->valueAttribute());
}

//  QOpcUa::UaStatusCode QOpcUaNode::attributeError(QOpcUa::NodeAttribute
//      attribute) const
extern "C" Q_DECL_EXPORT
QOpcUa::UaStatusCode ritual_ZNK10QOpcUaNode14attributeErrorEN6QOpcUa13NodeAttributeE(
    const QOpcUaNode *self,
    QOpcUa::NodeAttribute attribute) {
  return self->attributeError(attribute);
}

//  QOpcUa::UaStatusCode QOpcUaNode::valueAttributeError() const
extern "C" Q_DECL_EXPORT
QOpcUa::UaStatusCode ritual_ZNK10QOpcUaNode19valueAttributeErrorEv(
    const QOpcUaNode *self) {
  return self->valueAttributeError();
}

//  QDateTime QOpcUaNode::sourceTimestamp(QOpcUa::NodeAttribute attribute)
//      const
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZNK10QOpcUaNode15sourceTimestampEN6QOpcUa13NodeAttributeE(
    const QOpcUaNode *self,
    QOpcUa::NodeAttribute attribute) {
  return new QDateTime(self->sourceTimestamp(attribute));
}

//  QDateTime QOpcUaNode::serverTimestamp(QOpcUa::NodeAttribute attribute)
//      const
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZNK10QOpcUaNode15serverTimestampEN6QOpcUa13NodeAttributeE(
    const QOpcUaNode *self,
    QOpcUa::NodeAttribute attribute) {
  return new QDateTime(self->serverTimestamp(attribute));
}

//  bool QOpcUaNode::writeAttribute(QOpcUa::NodeAttribute attribute, const
//      QVariant &value, QOpcUa::Types type)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QOpcUaNode14writeAttributeEN6QOpcUa13NodeAttributeERK8QVariantNS0_5TypesE(
    QOpcUaNode *self,
    QOpcUa::NodeAttribute attribute,
    const QVariant *value,
    QOpcUa::Types type) {
  return self->writeAttribute(attribute, *value, type);
}

//  bool QOpcUaNode::writeAttributeRange(QOpcUa::NodeAttribute attribute,
//      const QVariant &value, const QString &indexRange, QOpcUa::Types type)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QOpcUaNode19writeAttributeRangeEN6QOpcUa13NodeAttributeERK8QVariantRK7QStringNS0_5TypesE(
    QOpcUaNode *self,
    QOpcUa::NodeAttribute attribute,
    const QVariant *value,
    const QString *indexRange,
    QOpcUa::Types type) {
  return self->writeAttributeRange(attribute, *value, *indexRange, type);
}

//  bool QOpcUaNode::writeAttributes(const AttributeMap &toWrite,
//      QOpcUa::Types valueAttributeType)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QOpcUaNode15writeAttributesERK4QMapIN6QOpcUa13NodeAttributeE8QVariantENS1_5TypesE(
    QOpcUaNode *self,
    const QOpcUaNode::AttributeMap *toWrite,
    QOpcUa::Types valueAttributeType) {
  return self->writeAttributes(*toWrite, valueAttributeType);
}

//  bool QOpcUaNode::writeValueAttribute(const QVariant &value, QOpcUa::Types
//      type)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QOpcUaNode19writeValueAttributeERK8QVariantN6QOpcUa5TypesE(
    QOpcUaNode *self,
    const QVariant *value,
    QOpcUa::Types type) {
  return self->writeValueAttribute(*value, type);
}

//  bool QOpcUaNode::enableMonitoring(QOpcUa::NodeAttributes attr, const
//      QOpcUaMonitoringParameters &settings)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QOpcUaNode16enableMonitoringE6QFlagsIN6QOpcUa13NodeAttributeEERK26QOpcUaMonitoringParameters(
    QOpcUaNode *self,
    int attr,
    const QOpcUaMonitoringParameters *settings) {
  return self->enableMonitoring(
      QFlags<QOpcUa::NodeAttribute>::fromInt(attr),
      *settings);
}

//  bool QOpcUaNode::disableMonitoring(QOpcUa::NodeAttributes attr)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QOpcUaNode17disableMonitoringE6QFlagsIN6QOpcUa13NodeAttributeEE(
    QOpcUaNode *self,
    int attr) {
  return self->disableMonitoring(
      QFlags<QOpcUa::NodeAttribute>::fromInt(attr));
}

//  bool QOpcUaNode::modifyMonitoring(QOpcUa::NodeAttribute attr,
//      QOpcUaMonitoringParameters::Parameter item, const QVariant &value)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QOpcUaNode16modifyMonitoringEN6QOpcUa13NodeAttributeEN26QOpcUaMonitoringParameters9ParameterERK8QVariant(
    QOpcUaNode *self,
    QOpcUa::NodeAttribute attr,
    QOpcUaMonitoringParameters::Parameter item,
    const QVariant *value) {
  return self->modifyMonitoring(attr, item, *value);
}

//  QOpcUaMonitoringParameters
//      QOpcUaNode::monitoringStatus(QOpcUa::NodeAttribute attr)
extern "C" Q_DECL_EXPORT
QOpcUaMonitoringParameters *ritual_ZN10QOpcUaNode16monitoringStatusEN6QOpcUa13NodeAttributeE(
    QOpcUaNode *self,
    QOpcUa::NodeAttribute attr) {
  return new QOpcUaMonitoringParameters(self->monitoringStatus(attr));
}

//  bool QOpcUaNode::modifyEventFilter(const
//      QOpcUaMonitoringParameters::EventFilter &eventFilter)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QOpcUaNode17modifyEventFilterERKN26QOpcUaMonitoringParameters11EventFilterE(
    QOpcUaNode *self,
    const QOpcUaMonitoringParameters::EventFilter *eventFilter) {
  return self->modifyEventFilter(*eventFilter);
}

//  bool QOpcUaNode::modifyDataChangeFilter(QOpcUa::NodeAttribute attr, const
//      QOpcUaMonitoringParameters::DataChangeFilter &filter)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QOpcUaNode22modifyDataChangeFilterEN6QOpcUa13NodeAttributeERKN26QOpcUaMonitoringParameters16DataChangeFilterE(
    QOpcUaNode *self,
    QOpcUa::NodeAttribute attr,
    const QOpcUaMonitoringParameters::DataChangeFilter *filter) {
  return self->modifyDataChangeFilter(attr, *filter);
}

//  bool QOpcUaNode::browseChildren(QOpcUa::ReferenceTypeId referenceType,
//      QOpcUa::NodeClasses nodeClassMask)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QOpcUaNode14browseChildrenEN6QOpcUa15ReferenceTypeIdE6QFlagsINS0_9NodeClassEE(
    QOpcUaNode *self,
    QOpcUa::ReferenceTypeId referenceType,
    int nodeClassMask) {
  return self->browseChildren(
      referenceType,
      QFlags<QOpcUa::NodeClass>::fromInt(nodeClassMask));
}

//  QString QOpcUaNode::nodeId() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK10QOpcUaNode6nodeIdEv(const QOpcUaNode *self) {
  return new QString(self->nodeId());
}

//  QOpcUaClient *QOpcUaNode::client() const
extern "C" Q_DECL_EXPORT
QOpcUaClient *ritual_ZNK10QOpcUaNode6clientEv(const QOpcUaNode *self) {
  return self->client();
}

//  bool QOpcUaNode::callMethod(const QString &methodNodeId, const
//      QList<QOpcUa::TypedVariant> &args)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QOpcUaNode10callMethodERK7QStringRK5QListISt4pairI8QVariantN6QOpcUa5TypesEEE(
    QOpcUaNode *self,
    const QString *methodNodeId,
    const QList<QOpcUa::TypedVariant> *args) {
  return self->callMethod(*methodNodeId, *args);
}

//  bool QOpcUaNode::resolveBrowsePath(const QList<QOpcUaRelativePathElement>
//      &path)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QOpcUaNode17resolveBrowsePathERK5QListI25QOpcUaRelativePathElementE(
    QOpcUaNode *self,
    const QList<QOpcUaRelativePathElement> *path) {
  return self->resolveBrowsePath(*path);
}

//  bool QOpcUaNode::browse(const QOpcUaBrowseRequest &request)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QOpcUaNode6browseERK19QOpcUaBrowseRequest(
    QOpcUaNode *self,
    const QOpcUaBrowseRequest *request) {
  return self->browse(*request);
}

//  QOpcUaHistoryReadResponse *QOpcUaNode::readHistoryRaw(const QDateTime
//      &startTime, const QDateTime &endTime, quint32 numValues, bool
//      returnBounds)
extern "C" Q_DECL_EXPORT
QOpcUaHistoryReadResponse *ritual_ZN10QOpcUaNode14readHistoryRawERK9QDateTimeS2_jb(
    QOpcUaNode *self,
    const QDateTime *startTime,
    const QDateTime *endTime,
    quint32 numValues,
    bool returnBounds) {
  return self->readHistoryRaw(*startTime, *endTime, numValues, returnBounds);
}

//  QOpcUaHistoryReadResponse *QOpcUaNode::readHistoryRaw(const QDateTime
//      &startTime, const QDateTime &endTime, quint32 numValues, bool
//      returnBounds, QOpcUa::TimestampsToReturn timestampsToReturn)
extern "C" Q_DECL_EXPORT
QOpcUaHistoryReadResponse *ritual_ZN10QOpcUaNode14readHistoryRawERK9QDateTimeS2_jbN6QOpcUa18TimestampsToReturnE(
    QOpcUaNode *self,
    const QDateTime *startTime,
    const QDateTime *endTime,
    quint32 numValues,
    bool returnBounds,
    QOpcUa::TimestampsToReturn timestampsToReturn) {
  return self->readHistoryRaw(
      *startTime,
      *endTime,
      numValues,
      returnBounds,
      timestampsToReturn);
}

//  QOpcUaHistoryReadResponse *QOpcUaNode::readHistoryEvents(const QDateTime
//      &startTime, const QDateTime &endTime,
//      QOpcUaMonitoringParameters::EventFilter &filter, quint32 numValues)
extern "C" Q_DECL_EXPORT
QOpcUaHistoryReadResponse *ritual_ZN10QOpcUaNode17readHistoryEventsERK9QDateTimeS2_RN26QOpcUaMonitoringParameters11EventFilterEj(
    QOpcUaNode *self,
    const QDateTime *startTime,
    const QDateTime *endTime,
    QOpcUaMonitoringParameters::EventFilter *filter,
    quint32 numValues) {
  return self->readHistoryEvents(*startTime, *endTime, *filter, numValues);
}

//  void QOpcUaNode::attributeRead(QOpcUa::NodeAttributes attributes)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QOpcUaNode13attributeReadE6QFlagsIN6QOpcUa13NodeAttributeEE(
    QOpcUaNode *self,
    int attributes) {
  self->attributeRead(QFlags<QOpcUa::NodeAttribute>::fromInt(attributes));
}

//  void QOpcUaNode::attributeWritten(QOpcUa::NodeAttribute attribute,
//      QOpcUa::UaStatusCode statusCode)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QOpcUaNode16attributeWrittenEN6QOpcUa13NodeAttributeENS0_12UaStatusCodeE(
    QOpcUaNode *self,
    QOpcUa::NodeAttribute attribute,
    QOpcUa::UaStatusCode statusCode) {
  self->attributeWritten(attribute, statusCode);
}

//  void QOpcUaNode::dataChangeOccurred(QOpcUa::NodeAttribute attr, QVariant
//      value)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QOpcUaNode18dataChangeOccurredEN6QOpcUa13NodeAttributeE8QVariant(
    QOpcUaNode *self,
    QOpcUa::NodeAttribute attr,
    const QVariant *value) {
  self->dataChangeOccurred(attr, *value);
}

//  void QOpcUaNode::attributeUpdated(QOpcUa::NodeAttribute attr, QVariant
//      value)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QOpcUaNode16attributeUpdatedEN6QOpcUa13NodeAttributeE8QVariant(
    QOpcUaNode *self,
    QOpcUa::NodeAttribute attr,
    const QVariant *value) {
  self->attributeUpdated(attr, *value);
}

//  void QOpcUaNode::valueAttributeUpdated(const QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QOpcUaNode21valueAttributeUpdatedERK8QVariant(
    QOpcUaNode *self,
    const QVariant *value) {
  self->valueAttributeUpdated(*value);
}

//  void QOpcUaNode::eventOccurred(QVariantList eventFields)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QOpcUaNode13eventOccurredE5QListI8QVariantE(
    QOpcUaNode *self,
    const QList<QVariant> *eventFields) {
  self->eventOccurred(*eventFields);
}

//  void QOpcUaNode::monitoringStatusChanged(QOpcUa::NodeAttribute attr,
//      QOpcUaMonitoringParameters::Parameters items, QOpcUa::UaStatusCode
//      statusCode)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QOpcUaNode23monitoringStatusChangedEN6QOpcUa13NodeAttributeE6QFlagsIN26QOpcUaMonitoringParameters9ParameterEENS0_12UaStatusCodeE(
    QOpcUaNode *self,
    QOpcUa::NodeAttribute attr,
    int items,
    QOpcUa::UaStatusCode statusCode) {
  self->monitoringStatusChanged(
      attr,
      QFlags<QOpcUaMonitoringParameters::Parameter>::fromInt(items),
      statusCode);
}

//  void QOpcUaNode::enableMonitoringFinished(QOpcUa::NodeAttribute attr,
//      QOpcUa::UaStatusCode statusCode)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QOpcUaNode24enableMonitoringFinishedEN6QOpcUa13NodeAttributeENS0_12UaStatusCodeE(
    QOpcUaNode *self,
    QOpcUa::NodeAttribute attr,
    QOpcUa::UaStatusCode statusCode) {
  self->enableMonitoringFinished(attr, statusCode);
}

//  void QOpcUaNode::disableMonitoringFinished(QOpcUa::NodeAttribute attr,
//      QOpcUa::UaStatusCode statusCode)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QOpcUaNode25disableMonitoringFinishedEN6QOpcUa13NodeAttributeENS0_12UaStatusCodeE(
    QOpcUaNode *self,
    QOpcUa::NodeAttribute attr,
    QOpcUa::UaStatusCode statusCode) {
  self->disableMonitoringFinished(attr, statusCode);
}

//  void QOpcUaNode::methodCallFinished(QString methodNodeId, QVariant
//      result, QOpcUa::UaStatusCode statusCode)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QOpcUaNode18methodCallFinishedE7QString8QVariantN6QOpcUa12UaStatusCodeE(
    QOpcUaNode *self,
    const QString *methodNodeId,
    const QVariant *result,
    QOpcUa::UaStatusCode statusCode) {
  self->methodCallFinished(*methodNodeId, *result, statusCode);
}

//  void QOpcUaNode::browseFinished(QList<QOpcUaReferenceDescription>
//      children, QOpcUa::UaStatusCode statusCode)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QOpcUaNode14browseFinishedE5QListI26QOpcUaReferenceDescriptionEN6QOpcUa12UaStatusCodeE(
    QOpcUaNode *self,
    const QList<QOpcUaReferenceDescription> *children,
    QOpcUa::UaStatusCode statusCode) {
  self->browseFinished(*children, statusCode);
}

//  void QOpcUaNode::resolveBrowsePathFinished(QList<QOpcUaBrowsePathTarget>
//      targets, QList<QOpcUaRelativePathElement> path, QOpcUa::UaStatusCode
//      statusCode)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QOpcUaNode25resolveBrowsePathFinishedE5QListI22QOpcUaBrowsePathTargetES0_I25QOpcUaRelativePathElementEN6QOpcUa12UaStatusCodeE(
    QOpcUaNode *self,
    const QList<QOpcUaBrowsePathTarget> *targets,
    const QList<QOpcUaRelativePathElement> *path,
    QOpcUa::UaStatusCode statusCode) {
  self->resolveBrowsePathFinished(*targets, *path, statusCode);
}

//  a Python function taken by a CuteQOpcUaNode, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QOpcUaNode(QOpcUaNode *self, const char *key, void *call) {
  return static_cast<CuteQOpcUaNode *>(self)->take(key, call);
}
