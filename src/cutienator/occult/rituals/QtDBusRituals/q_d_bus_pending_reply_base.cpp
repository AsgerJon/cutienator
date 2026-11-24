//  Written by dev_tooling.RitualGenerator from the records of
//  QtDBus/qdbuspendingreply.h, Qt 6.12.0. Changes made here are lost.
#include <QtDBus/qtdbusglobal.h>
#if !defined(QT_NO_DBUS)
#include <QtDBus/qdbuspendingreply.h>
#include <QtDBus/qdbuspendingcall.h>
#include <QtDBus/qdbusmessage.h>
#include <QtCore/qvariant.h>

//  QDBusPendingReplyBase::QDBusPendingReplyBase()
extern "C" Q_DECL_EXPORT
QDBusPendingReplyBase *ritual_ZN21QDBusPendingReplyBaseC1Ev() {
  return new QDBusPendingReplyBase();
}

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
//  QDBusPendingReplyBase::~QDBusPendingReplyBase()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QDBusPendingReplyBaseD1Ev(QDBusPendingReplyBase *self) {
  delete self;
}
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)

//  void QDBusPendingReplyBase::assign(const QDBusPendingCall &call)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QDBusPendingReplyBase6assignERK16QDBusPendingCall(
    QDBusPendingReplyBase *self,
    const QDBusPendingCall *call) {
  self->assign(*call);
}

//  void QDBusPendingReplyBase::assign(const QDBusMessage &message)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QDBusPendingReplyBase6assignERK12QDBusMessage(
    QDBusPendingReplyBase *self,
    const QDBusMessage *message) {
  self->assign(*message);
}

//  QVariant QDBusPendingReplyBase::argumentAt(int index) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK21QDBusPendingReplyBase10argumentAtEi(
    const QDBusPendingReplyBase *self,
    int index) {
  return new QVariant(self->argumentAt(index));
}

//  void QDBusPendingReplyBase::setMetaTypes(int count, const QMetaType
//      *metaTypes)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QDBusPendingReplyBase12setMetaTypesEiPK9QMetaType(
    QDBusPendingReplyBase *self,
    int count,
    const QMetaType *metaTypes) {
  self->setMetaTypes(count, metaTypes);
}

#endif  // !defined(QT_NO_DBUS)
