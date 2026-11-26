//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/6.12.0/QtNetwork/private/qdnslookup_p.h, Qt 6.12.0. Edited by
//  hand on 2026-11-25: added by hand, instances of templates of the class:
//  2. Kept as it is when the generator runs again.
#include <QtNetwork/qtnetworkglobal.h>
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#if QT_CONFIG(dnslookup)
#if QT_CONFIG(dnslookup)
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#include <QtNetwork/QtNetwork>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/6.12.0/QtNetwork/private/qdnslookup_p.h>
#include <QtCore/qstring.h>
#include <QtCore/qstringview.h>
#include <QtCore/qlatin1stringview.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  const QMetaObject *QDnsLookupRunnable::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QDnsLookupRunnable10metaObjectEv(
    const QDnsLookupRunnable *self) {
  return self->metaObject();
}

//  void *QDnsLookupRunnable::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN18QDnsLookupRunnable11qt_metacastEPKc(
    QDnsLookupRunnable *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QDnsLookupRunnable::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN18QDnsLookupRunnable11qt_metacallEN11QMetaObject4CallEiPPv(
    QDnsLookupRunnable *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  void QDnsLookupRunnable::run()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QDnsLookupRunnable3runEv(QDnsLookupRunnable *self) {
  self->run();
}

//  void QDnsLookupRunnable::finished(const QDnsLookupReply &reply)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QDnsLookupRunnable8finishedERK15QDnsLookupReply(
    QDnsLookupRunnable *self,
    const QDnsLookupReply *reply) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QDnsLookupRunnable")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "finished(const QDnsLookupReply &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "finished(const QDnsLookupReply &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(reply)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  QDnsLookupRunnable as the QRunnable it is built on
extern "C" Q_DECL_EXPORT
QRunnable *ritual_cast_QDnsLookupRunnable_QRunnable(
    QDnsLookupRunnable *self) {
  return static_cast<QRunnable *>(self);
}

//  QString QDnsLookupRunnable::decodeLabel<QStringView>(
//      QStringView encodedLabel)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18QDnsLookupRunnable11decodeLabelI11QStringViewEE7QStringT_(
    const QString *encodedLabel) {
  return new QString(
      QDnsLookupRunnable::decodeLabel<QStringView>(
          QStringView(*encodedLabel)));
}

//  QString QDnsLookupRunnable::decodeLabel<QLatin1StringView>(
//      QLatin1StringView encodedLabel)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18QDnsLookupRunnable11decodeLabelI13QLatin1StringEE7QStringT_(
    const char *encodedLabel) {
  return new QString(
      QDnsLookupRunnable::decodeLabel<QLatin1StringView>(
          QLatin1StringView(encodedLabel)));
}

#endif  // QT_CONFIG(dnslookup)
#endif  // QT_CONFIG(dnslookup)
