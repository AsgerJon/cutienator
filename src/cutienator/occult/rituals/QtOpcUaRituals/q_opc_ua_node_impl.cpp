//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpcUa/6.12.0/QtOpcUa/private/qopcuanodeimpl_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtOpcUa/QtOpcUa>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtOpcUa/6.12.0/QtOpcUa/private/qopcuanodeimpl_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtOpcUa/qopcuamonitoringparameters.h>
#include <QtOpcUa/qopcuabrowserequest.h>
#include <QtCore/qvariant.h>
#include <QtCore/qdatetime.h>
#include <QtOpcUa/qopcuarelativepathelement.h>
#include <QtOpcUa/qopcuareadresult.h>
#include <QtOpcUa/qopcuareferencedescription.h>
#include <QtOpcUa/qopcuabrowsepathtarget.h>
#include <QtOpcUa/qopcuahistorydata.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QOpcUaNodeImpl that Python can take functions over in. Every QOpcUaNodeImpl
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQOpcUaNodeImplCall0)(const void *, int, const QString *, int *);
typedef bool (*CuteQOpcUaNodeImplCall1)(const void *, int, const QOpcUaMonitoringParameters *, int *);
typedef bool (*CuteQOpcUaNodeImplCall2)(const void *, int, int *);
typedef bool (*CuteQOpcUaNodeImplCall3)(const void *, const QOpcUaBrowseRequest *, int *);
typedef QString * (*CuteQOpcUaNodeImplCall4)(const void *, int *);
typedef bool (*CuteQOpcUaNodeImplCall5)(const void *, int, const QVariant *, int, const QString *, int *);
typedef bool (*CuteQOpcUaNodeImplCall6)(const void *, int, int, const QVariant *, int *);
typedef void * (*CuteQOpcUaNodeImplCall7)(const void *, const QDateTime *, const QDateTime *, quint32, bool, int, int *);
typedef void * (*CuteQOpcUaNodeImplCall8)(const void *, const QDateTime *, const QDateTime *, const QOpcUaMonitoringParameters::EventFilter *, quint32, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQOpcUaNodeImplCall9)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQOpcUaNodeImplCall10)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQOpcUaNodeImplCall11)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQOpcUaNodeImplCall12)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQOpcUaNodeImplCall13)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQOpcUaNodeImplCall14)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQOpcUaNodeImplCall15)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQOpcUaNodeImpl : public QOpcUaNodeImpl {
public:
  using QOpcUaNodeImpl::QOpcUaNodeImpl;
  void *taken[16] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN14QOpcUaNodeImpl14readAttributesE6QFlagsIN6QOpcUa13NodeAttributeEERK7QString")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QOpcUaNodeImpl16enableMonitoringE6QFlagsIN6QOpcUa13NodeAttributeEERK26QOpcUaMonitoringParameters")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QOpcUaNodeImpl17disableMonitoringE6QFlagsIN6QOpcUa13NodeAttributeEE")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QOpcUaNodeImpl6browseERK19QOpcUaBrowseRequest")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QOpcUaNodeImpl6nodeIdEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QOpcUaNodeImpl14writeAttributeEN6QOpcUa13NodeAttributeERK8QVariantNS0_5TypesERK7QString")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QOpcUaNodeImpl16modifyMonitoringEN6QOpcUa13NodeAttributeEN26QOpcUaMonitoringParameters9ParameterERK8QVariant")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QOpcUaNodeImpl14readHistoryRawERK9QDateTimeS2_jbN6QOpcUa18TimestampsToReturnE")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QOpcUaNodeImpl17readHistoryEventsERK9QDateTimeS2_RKN26QOpcUaMonitoringParameters11EventFilterEj")) {
      taken[8] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[13] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[14] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[15] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  bool QOpcUaNodeImpl::readAttributes(QOpcUa::NodeAttributes attr,
  //      const QString &indexRange)
  bool readAttributes(
      QOpcUa::NodeAttributes attr,
      const QString &indexRange) override {
    if (taken[0]) {
      int handled = 0;
      CuteQOpcUaNodeImplCall0 call = reinterpret_cast<CuteQOpcUaNodeImplCall0>(taken[0]);
      bool given = call(this, static_cast<int>(attr.toInt()), &indexRange, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  bool QOpcUaNodeImpl::enableMonitoring(QOpcUa::NodeAttributes attr,
  //      const QOpcUaMonitoringParameters &settings)
  bool enableMonitoring(
      QOpcUa::NodeAttributes attr,
      const QOpcUaMonitoringParameters &settings) override {
    if (taken[1]) {
      int handled = 0;
      CuteQOpcUaNodeImplCall1 call = reinterpret_cast<CuteQOpcUaNodeImplCall1>(taken[1]);
      bool given = call(this, static_cast<int>(attr.toInt()), &settings, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  bool QOpcUaNodeImpl::disableMonitoring(QOpcUa::NodeAttributes attr)
  bool disableMonitoring(QOpcUa::NodeAttributes attr) override {
    if (taken[2]) {
      int handled = 0;
      CuteQOpcUaNodeImplCall2 call = reinterpret_cast<CuteQOpcUaNodeImplCall2>(taken[2]);
      bool given = call(this, static_cast<int>(attr.toInt()), &handled);
      if (handled) return given;
    }
    return {};
  }

  //  bool QOpcUaNodeImpl::browse(const QOpcUaBrowseRequest &request)
  bool browse(const QOpcUaBrowseRequest &request) override {
    if (taken[3]) {
      int handled = 0;
      CuteQOpcUaNodeImplCall3 call = reinterpret_cast<CuteQOpcUaNodeImplCall3>(taken[3]);
      bool given = call(this, &request, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  QString QOpcUaNodeImpl::nodeId() const
  QString nodeId() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQOpcUaNodeImplCall4 call = reinterpret_cast<CuteQOpcUaNodeImplCall4>(taken[4]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return {};
  }

  //  bool QOpcUaNodeImpl::writeAttribute(QOpcUa::NodeAttribute attribute,
  //      const QVariant &value, QOpcUa::Types type, const QString
  //      &indexRange)
  bool writeAttribute(
      QOpcUa::NodeAttribute attribute,
      const QVariant &value,
      QOpcUa::Types type,
      const QString &indexRange) override {
    if (taken[5]) {
      int handled = 0;
      CuteQOpcUaNodeImplCall5 call = reinterpret_cast<CuteQOpcUaNodeImplCall5>(taken[5]);
      bool given = call(this, static_cast<int>(attribute), &value, static_cast<int>(type), &indexRange, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  bool QOpcUaNodeImpl::modifyMonitoring(QOpcUa::NodeAttribute attr,
  //      QOpcUaMonitoringParameters::Parameter item, const QVariant
  //      &value)
  bool modifyMonitoring(
      QOpcUa::NodeAttribute attr,
      QOpcUaMonitoringParameters::Parameter item,
      const QVariant &value) override {
    if (taken[6]) {
      int handled = 0;
      CuteQOpcUaNodeImplCall6 call = reinterpret_cast<CuteQOpcUaNodeImplCall6>(taken[6]);
      bool given = call(this, static_cast<int>(attr), static_cast<int>(item), &value, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  QOpcUaHistoryReadResponse *QOpcUaNodeImpl::readHistoryRaw(const
  //      QDateTime &startTime, const QDateTime &endTime, quint32
  //      numValues, bool returnBounds, QOpcUa::TimestampsToReturn
  //      timestampsToReturn)
  QOpcUaHistoryReadResponse *readHistoryRaw(
      const QDateTime &startTime,
      const QDateTime &endTime,
      quint32 numValues,
      bool returnBounds,
      QOpcUa::TimestampsToReturn timestampsToReturn) override {
    if (taken[7]) {
      int handled = 0;
      CuteQOpcUaNodeImplCall7 call = reinterpret_cast<CuteQOpcUaNodeImplCall7>(taken[7]);
      void * given = call(this, &startTime, &endTime, numValues, returnBounds, static_cast<int>(timestampsToReturn), &handled);
      if (handled) return static_cast<QOpcUaHistoryReadResponse *>(given);
    }
    return {};
  }

  //  QOpcUaHistoryReadResponse *QOpcUaNodeImpl::readHistoryEvents(const
  //      QDateTime &startTime, const QDateTime &endTime, const
  //      QOpcUaMonitoringParameters::EventFilter &filter, quint32
  //      numValues)
  QOpcUaHistoryReadResponse *readHistoryEvents(
      const QDateTime &startTime,
      const QDateTime &endTime,
      const QOpcUaMonitoringParameters::EventFilter &filter,
      quint32 numValues) override {
    if (taken[8]) {
      int handled = 0;
      CuteQOpcUaNodeImplCall8 call = reinterpret_cast<CuteQOpcUaNodeImplCall8>(taken[8]);
      void * given = call(this, &startTime, &endTime, &filter, numValues, &handled);
      if (handled) return static_cast<QOpcUaHistoryReadResponse *>(given);
    }
    return {};
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQOpcUaNodeImplCall9 call = reinterpret_cast<CuteQOpcUaNodeImplCall9>(taken[9]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQOpcUaNodeImplCall10 call = reinterpret_cast<CuteQOpcUaNodeImplCall10>(taken[10]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQOpcUaNodeImplCall11 call = reinterpret_cast<CuteQOpcUaNodeImplCall11>(taken[11]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQOpcUaNodeImplCall12 call = reinterpret_cast<CuteQOpcUaNodeImplCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQOpcUaNodeImplCall13 call = reinterpret_cast<CuteQOpcUaNodeImplCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[14]) {
      int handled = 0;
      CuteQOpcUaNodeImplCall14 call = reinterpret_cast<CuteQOpcUaNodeImplCall14>(taken[14]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[15]) {
      int handled = 0;
      CuteQOpcUaNodeImplCall15 call = reinterpret_cast<CuteQOpcUaNodeImplCall15>(taken[15]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QOpcUaNodeImpl::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK14QOpcUaNodeImpl10metaObjectEv(
    const QOpcUaNodeImpl *self) {
  return self->metaObject();
}

//  void *QOpcUaNodeImpl::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN14QOpcUaNodeImpl11qt_metacastEPKc(
    QOpcUaNodeImpl *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QOpcUaNodeImpl::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN14QOpcUaNodeImpl11qt_metacallEN11QMetaObject4CallEiPPv(
    QOpcUaNodeImpl *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QOpcUaNodeImpl::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14QOpcUaNodeImpl2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QOpcUaNodeImpl::tr(s, c, n));
}

//  QOpcUaNodeImpl::~QOpcUaNodeImpl()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QOpcUaNodeImplD1Ev(QOpcUaNodeImpl *self) {
  delete self;
}

//  bool QOpcUaNodeImpl::readAttributes(QOpcUa::NodeAttributes attr, const
//      QString &indexRange)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QOpcUaNodeImpl14readAttributesE6QFlagsIN6QOpcUa13NodeAttributeEERK7QString(
    QOpcUaNodeImpl *self,
    int attr,
    const QString *indexRange) {
  return self->readAttributes(
      QFlags<QOpcUa::NodeAttribute>::fromInt(attr),
      *indexRange);
}

//  bool QOpcUaNodeImpl::enableMonitoring(QOpcUa::NodeAttributes attr, const
//      QOpcUaMonitoringParameters &settings)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QOpcUaNodeImpl16enableMonitoringE6QFlagsIN6QOpcUa13NodeAttributeEERK26QOpcUaMonitoringParameters(
    QOpcUaNodeImpl *self,
    int attr,
    const QOpcUaMonitoringParameters *settings) {
  return self->enableMonitoring(
      QFlags<QOpcUa::NodeAttribute>::fromInt(attr),
      *settings);
}

//  bool QOpcUaNodeImpl::disableMonitoring(QOpcUa::NodeAttributes attr)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QOpcUaNodeImpl17disableMonitoringE6QFlagsIN6QOpcUa13NodeAttributeEE(
    QOpcUaNodeImpl *self,
    int attr) {
  return self->disableMonitoring(
      QFlags<QOpcUa::NodeAttribute>::fromInt(attr));
}

//  bool QOpcUaNodeImpl::browse(const QOpcUaBrowseRequest &request)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QOpcUaNodeImpl6browseERK19QOpcUaBrowseRequest(
    QOpcUaNodeImpl *self,
    const QOpcUaBrowseRequest *request) {
  return self->browse(*request);
}

//  QString QOpcUaNodeImpl::nodeId() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QOpcUaNodeImpl6nodeIdEv(const QOpcUaNodeImpl *self) {
  return new QString(self->nodeId());
}

//  bool QOpcUaNodeImpl::writeAttribute(QOpcUa::NodeAttribute attribute,
//      const QVariant &value, QOpcUa::Types type, const QString &indexRange)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QOpcUaNodeImpl14writeAttributeEN6QOpcUa13NodeAttributeERK8QVariantNS0_5TypesERK7QString(
    QOpcUaNodeImpl *self,
    QOpcUa::NodeAttribute attribute,
    const QVariant *value,
    QOpcUa::Types type,
    const QString *indexRange) {
  return self->writeAttribute(attribute, *value, type, *indexRange);
}

//  bool QOpcUaNodeImpl::writeAttributes(const QOpcUaNode::AttributeMap
//      &toWrite, QOpcUa::Types valueAttributeType)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QOpcUaNodeImpl15writeAttributesERK4QMapIN6QOpcUa13NodeAttributeE8QVariantENS1_5TypesE(
    QOpcUaNodeImpl *self,
    const QOpcUaNode::AttributeMap *toWrite,
    QOpcUa::Types valueAttributeType) {
  return self->writeAttributes(*toWrite, valueAttributeType);
}

//  bool QOpcUaNodeImpl::modifyMonitoring(QOpcUa::NodeAttribute attr,
//      QOpcUaMonitoringParameters::Parameter item, const QVariant &value)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QOpcUaNodeImpl16modifyMonitoringEN6QOpcUa13NodeAttributeEN26QOpcUaMonitoringParameters9ParameterERK8QVariant(
    QOpcUaNodeImpl *self,
    QOpcUa::NodeAttribute attr,
    QOpcUaMonitoringParameters::Parameter item,
    const QVariant *value) {
  return self->modifyMonitoring(attr, item, *value);
}

//  bool QOpcUaNodeImpl::callMethod(const QString &methodNodeId, const
//      QList<QOpcUa::TypedVariant> &args)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QOpcUaNodeImpl10callMethodERK7QStringRK5QListISt4pairI8QVariantN6QOpcUa5TypesEEE(
    QOpcUaNodeImpl *self,
    const QString *methodNodeId,
    const QList<QOpcUa::TypedVariant> *args) {
  return self->callMethod(*methodNodeId, *args);
}

//  QOpcUaHistoryReadResponse *QOpcUaNodeImpl::readHistoryRaw(const QDateTime
//      &startTime, const QDateTime &endTime, quint32 numValues, bool
//      returnBounds, QOpcUa::TimestampsToReturn timestampsToReturn)
extern "C" Q_DECL_EXPORT
QOpcUaHistoryReadResponse *ritual_ZN14QOpcUaNodeImpl14readHistoryRawERK9QDateTimeS2_jbN6QOpcUa18TimestampsToReturnE(
    QOpcUaNodeImpl *self,
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

//  QOpcUaHistoryReadResponse *QOpcUaNodeImpl::readHistoryEvents(const
//      QDateTime &startTime, const QDateTime &endTime, const
//      QOpcUaMonitoringParameters::EventFilter &filter, quint32 numValues)
extern "C" Q_DECL_EXPORT
QOpcUaHistoryReadResponse *ritual_ZN14QOpcUaNodeImpl17readHistoryEventsERK9QDateTimeS2_RKN26QOpcUaMonitoringParameters11EventFilterEj(
    QOpcUaNodeImpl *self,
    const QDateTime *startTime,
    const QDateTime *endTime,
    const QOpcUaMonitoringParameters::EventFilter *filter,
    quint32 numValues) {
  return self->readHistoryEvents(*startTime, *endTime, *filter, numValues);
}

//  bool QOpcUaNodeImpl::resolveBrowsePath(const
//      QList<QOpcUaRelativePathElement> &path)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QOpcUaNodeImpl17resolveBrowsePathERK5QListI25QOpcUaRelativePathElementE(
    QOpcUaNodeImpl *self,
    const QList<QOpcUaRelativePathElement> *path) {
  return self->resolveBrowsePath(*path);
}

//  quint64 QOpcUaNodeImpl::handle() const
extern "C" Q_DECL_EXPORT
quint64 ritual_ZNK14QOpcUaNodeImpl6handleEv(const QOpcUaNodeImpl *self) {
  return self->handle();
}

//  void QOpcUaNodeImpl::setHandle(quint64 handle)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QOpcUaNodeImpl9setHandleEy(
    QOpcUaNodeImpl *self,
    quint64 handle) {
  self->setHandle(handle);
}

//  bool QOpcUaNodeImpl::registered() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QOpcUaNodeImpl10registeredEv(const QOpcUaNodeImpl *self) {
  return self->registered();
}

//  void QOpcUaNodeImpl::setRegistered(bool registered)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QOpcUaNodeImpl13setRegisteredEb(
    QOpcUaNodeImpl *self,
    bool registered) {
  self->setRegistered(registered);
}

//  void QOpcUaNodeImpl::attributesRead(QList<QOpcUaReadResult> attr,
//      QOpcUa::UaStatusCode serviceResult)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QOpcUaNodeImpl14attributesReadE5QListI16QOpcUaReadResultEN6QOpcUa12UaStatusCodeE(
    QOpcUaNodeImpl *self,
    const QList<QOpcUaReadResult> *attr,
    QOpcUa::UaStatusCode serviceResult) {
  self->attributesRead(*attr, serviceResult);
}

//  void QOpcUaNodeImpl::attributeWritten(QOpcUa::NodeAttribute attr,
//      QVariant value, QOpcUa::UaStatusCode statusCode)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QOpcUaNodeImpl16attributeWrittenEN6QOpcUa13NodeAttributeE8QVariantNS0_12UaStatusCodeE(
    QOpcUaNodeImpl *self,
    QOpcUa::NodeAttribute attr,
    const QVariant *value,
    QOpcUa::UaStatusCode statusCode) {
  self->attributeWritten(attr, *value, statusCode);
}

//  void QOpcUaNodeImpl::browseFinished(QList<QOpcUaReferenceDescription>
//      children, QOpcUa::UaStatusCode statusCode)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QOpcUaNodeImpl14browseFinishedE5QListI26QOpcUaReferenceDescriptionEN6QOpcUa12UaStatusCodeE(
    QOpcUaNodeImpl *self,
    const QList<QOpcUaReferenceDescription> *children,
    QOpcUa::UaStatusCode statusCode) {
  self->browseFinished(*children, statusCode);
}

//  void QOpcUaNodeImpl::dataChangeOccurred(QOpcUa::NodeAttribute attr,
//      QOpcUaReadResult value)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QOpcUaNodeImpl18dataChangeOccurredEN6QOpcUa13NodeAttributeE16QOpcUaReadResult(
    QOpcUaNodeImpl *self,
    QOpcUa::NodeAttribute attr,
    const QOpcUaReadResult *value) {
  self->dataChangeOccurred(attr, *value);
}

//  void QOpcUaNodeImpl::eventOccurred(QVariantList eventFields)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QOpcUaNodeImpl13eventOccurredE5QListI8QVariantE(
    QOpcUaNodeImpl *self,
    const QList<QVariant> *eventFields) {
  self->eventOccurred(*eventFields);
}

//  void QOpcUaNodeImpl::monitoringEnableDisable(QOpcUa::NodeAttribute attr,
//      bool subscribe, QOpcUaMonitoringParameters status)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QOpcUaNodeImpl23monitoringEnableDisableEN6QOpcUa13NodeAttributeEb26QOpcUaMonitoringParameters(
    QOpcUaNodeImpl *self,
    QOpcUa::NodeAttribute attr,
    bool subscribe,
    const QOpcUaMonitoringParameters *status) {
  self->monitoringEnableDisable(attr, subscribe, *status);
}

//  void QOpcUaNodeImpl::monitoringStatusChanged(QOpcUa::NodeAttribute attr,
//      QOpcUaMonitoringParameters::Parameters items,
//      QOpcUaMonitoringParameters param)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QOpcUaNodeImpl23monitoringStatusChangedEN6QOpcUa13NodeAttributeE6QFlagsIN26QOpcUaMonitoringParameters9ParameterEES3_(
    QOpcUaNodeImpl *self,
    QOpcUa::NodeAttribute attr,
    int items,
    const QOpcUaMonitoringParameters *param) {
  self->monitoringStatusChanged(
      attr,
      QFlags<QOpcUaMonitoringParameters::Parameter>::fromInt(items),
      *param);
}

//  void QOpcUaNodeImpl::methodCallFinished(QString methodNodeId, QVariant
//      result, QOpcUa::UaStatusCode statusCode)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QOpcUaNodeImpl18methodCallFinishedE7QString8QVariantN6QOpcUa12UaStatusCodeE(
    QOpcUaNodeImpl *self,
    const QString *methodNodeId,
    const QVariant *result,
    QOpcUa::UaStatusCode statusCode) {
  self->methodCallFinished(*methodNodeId, *result, statusCode);
}

//  void
//      QOpcUaNodeImpl::resolveBrowsePathFinished(QList<QOpcUaBrowsePathTarge
//      t> targets, QList<QOpcUaRelativePathElement> path,
//      QOpcUa::UaStatusCode status)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QOpcUaNodeImpl25resolveBrowsePathFinishedE5QListI22QOpcUaBrowsePathTargetES0_I25QOpcUaRelativePathElementEN6QOpcUa12UaStatusCodeE(
    QOpcUaNodeImpl *self,
    const QList<QOpcUaBrowsePathTarget> *targets,
    const QList<QOpcUaRelativePathElement> *path,
    QOpcUa::UaStatusCode status) {
  self->resolveBrowsePathFinished(*targets, *path, status);
}

//  void QOpcUaNodeImpl::readHistoryRawFinished(QList<QOpcUaHistoryData>
//      results, QOpcUa::UaStatusCode serviceResult)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QOpcUaNodeImpl22readHistoryRawFinishedE5QListI17QOpcUaHistoryDataEN6QOpcUa12UaStatusCodeE(
    QOpcUaNodeImpl *self,
    const QList<QOpcUaHistoryData> *results,
    QOpcUa::UaStatusCode serviceResult) {
  self->readHistoryRawFinished(*results, serviceResult);
}

//  a Python function taken by a CuteQOpcUaNodeImpl, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QOpcUaNodeImpl(
    QOpcUaNodeImpl *self,
    const char *key,
    void *call) {
  return static_cast<CuteQOpcUaNodeImpl *>(self)->take(key, call);
}
