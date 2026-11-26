//  Written by dev_tooling.RitualGenerator from the records of
//  QtNfc/6.12.0/QtNfc/private/qiosndefnotifier_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtNfc/qtnfcglobal.h>
#include <QtNfc/6.12.0/QtNfc/private/qtnfcglobal_p.h>
#if defined(Q_OS_IOS)
#include <QtNfc/6.12.0/QtNfc/private/qtnfcglobal_p.h>
#include <QtNfc/QtNfc>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNfc/6.12.0/QtNfc/private/qiosndefnotifier_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtNfc/qnearfieldtarget.h>
#include <QtNfc/qndefmessage.h>

//  const QMetaObject *QNfcNdefNotifier::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16QNfcNdefNotifier10metaObjectEv(
    const QNfcNdefNotifier *self) {
  return self->metaObject();
}

//  void *QNfcNdefNotifier::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN16QNfcNdefNotifier11qt_metacastEPKc(
    QNfcNdefNotifier *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QNfcNdefNotifier::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN16QNfcNdefNotifier11qt_metacallEN11QMetaObject4CallEiPPv(
    QNfcNdefNotifier *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QNfcNdefNotifier::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QNfcNdefNotifier2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QNfcNdefNotifier::tr(s, c, n));
}

//  QNfcNdefNotifier::QNfcNdefNotifier()
extern "C" Q_DECL_EXPORT
QNfcNdefNotifier *ritual_ZN16QNfcNdefNotifierC1Ev() {
  return new QNfcNdefNotifier();
}

//  void QNfcNdefNotifier::tagDetected(void *tag)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QNfcNdefNotifier11tagDetectedEPv(
    QNfcNdefNotifier *self,
    void *tag) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QNfcNdefNotifier")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "tagDetected(void *)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "tagDetected(void *)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&tag)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QNfcNdefNotifier::invalidateWithError(bool restart)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QNfcNdefNotifier19invalidateWithErrorEb(
    QNfcNdefNotifier *self,
    bool restart) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QNfcNdefNotifier")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "invalidateWithError(bool)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "invalidateWithError(bool)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&restart)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QNfcNdefNotifier::tagLost(void *tag)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QNfcNdefNotifier7tagLostEPv(
    QNfcNdefNotifier *self,
    void *tag) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QNfcNdefNotifier")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "tagLost(void *)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "tagLost(void *)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&tag)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QNfcNdefNotifier::tagError(QNearFieldTarget::Error code,
//      QNearFieldTarget::RequestId request)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QNfcNdefNotifier8tagErrorEN16QNearFieldTarget5ErrorENS0_9RequestIdE(
    QNfcNdefNotifier *self,
    QNearFieldTarget::Error code,
    const QNearFieldTarget::RequestId *request) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QNfcNdefNotifier")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "tagError(QNearFieldTarget::Error,QNearFieldTarget::RequestId)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "tagError(QNearFieldTarget::Error,QNearFieldTarget::RequestId)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&code)),
      const_cast<void *>(static_cast<const void *>(request)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QNfcNdefNotifier::ndefMessageWritten(QNearFieldTarget::RequestId
//      request)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QNfcNdefNotifier18ndefMessageWrittenEN16QNearFieldTarget9RequestIdE(
    QNfcNdefNotifier *self,
    const QNearFieldTarget::RequestId *request) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QNfcNdefNotifier")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "ndefMessageWritten(QNearFieldTarget::RequestId)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "ndefMessageWritten(QNearFieldTarget::RequestId)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(request)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QNfcNdefNotifier::ndefMessageRead(const QNdefMessage &message,
//      QNearFieldTarget::RequestId request)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QNfcNdefNotifier15ndefMessageReadERK12QNdefMessageN16QNearFieldTarget9RequestIdE(
    QNfcNdefNotifier *self,
    const QNdefMessage *message,
    const QNearFieldTarget::RequestId *request) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QNfcNdefNotifier")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "ndefMessageRead(const QNdefMessage &,QNearFieldTarget::RequestId)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "ndefMessageRead(const QNdefMessage &,QNearFieldTarget::RequestId)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(message)),
      const_cast<void *>(static_cast<const void *>(request)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

#endif  // defined(Q_OS_IOS)
