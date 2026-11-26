//  Written by dev_tooling.RitualGenerator from the records of
//  QtDBus/qdbusunixfiledescriptor.h, Qt 6.12.0. Changes made here are lost.
#include <QtDBus/qtdbusglobal.h>
#if !defined(QT_NO_DBUS)
#include <QtDBus/qdbusunixfiledescriptor.h>

//  QDBusUnixFileDescriptor::QDBusUnixFileDescriptor()
extern "C" Q_DECL_EXPORT
QDBusUnixFileDescriptor *ritual_ZN23QDBusUnixFileDescriptorC1Ev() {
  return new QDBusUnixFileDescriptor();
}

//  QDBusUnixFileDescriptor::QDBusUnixFileDescriptor(int fileDescriptor)
extern "C" Q_DECL_EXPORT
QDBusUnixFileDescriptor *ritual_ZN23QDBusUnixFileDescriptorC1Ei(
    int fileDescriptor) {
  return new QDBusUnixFileDescriptor(fileDescriptor);
}

//  QDBusUnixFileDescriptor::QDBusUnixFileDescriptor(const
//      QDBusUnixFileDescriptor &other)
extern "C" Q_DECL_EXPORT
QDBusUnixFileDescriptor *ritual_ZN23QDBusUnixFileDescriptorC1ERKS_(
    const QDBusUnixFileDescriptor *other) {
  return new QDBusUnixFileDescriptor(*other);
}

//  QDBusUnixFileDescriptor
//      &QDBusUnixFileDescriptor::operator=(QDBusUnixFileDescriptor &&other)
extern "C" Q_DECL_EXPORT
QDBusUnixFileDescriptor *ritual_ZN23QDBusUnixFileDescriptoraSEOS_(
    QDBusUnixFileDescriptor *self,
    QDBusUnixFileDescriptor *other) {
  return &(self->operator=(std::move(*other)));
}

//  QDBusUnixFileDescriptor &QDBusUnixFileDescriptor::operator=(const
//      QDBusUnixFileDescriptor &other)
extern "C" Q_DECL_EXPORT
QDBusUnixFileDescriptor *ritual_ZN23QDBusUnixFileDescriptoraSERKS_(
    QDBusUnixFileDescriptor *self,
    const QDBusUnixFileDescriptor *other) {
  return &(self->operator=(*other));
}

//  QDBusUnixFileDescriptor::~QDBusUnixFileDescriptor()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QDBusUnixFileDescriptorD1Ev(QDBusUnixFileDescriptor *self) {
  delete self;
}

//  void QDBusUnixFileDescriptor::swap(QDBusUnixFileDescriptor &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QDBusUnixFileDescriptor4swapERS_(
    QDBusUnixFileDescriptor *self,
    QDBusUnixFileDescriptor *other) {
  self->swap(*other);
}

//  bool QDBusUnixFileDescriptor::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QDBusUnixFileDescriptor7isValidEv(
    const QDBusUnixFileDescriptor *self) {
  return self->isValid();
}

//  int QDBusUnixFileDescriptor::fileDescriptor() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK23QDBusUnixFileDescriptor14fileDescriptorEv(
    const QDBusUnixFileDescriptor *self) {
  return self->fileDescriptor();
}

//  void QDBusUnixFileDescriptor::setFileDescriptor(int fileDescriptor)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QDBusUnixFileDescriptor17setFileDescriptorEi(
    QDBusUnixFileDescriptor *self,
    int fileDescriptor) {
  self->setFileDescriptor(fileDescriptor);
}

//  void QDBusUnixFileDescriptor::giveFileDescriptor(int fileDescriptor)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QDBusUnixFileDescriptor18giveFileDescriptorEi(
    QDBusUnixFileDescriptor *self,
    int fileDescriptor) {
  self->giveFileDescriptor(fileDescriptor);
}

//  int QDBusUnixFileDescriptor::takeFileDescriptor()
extern "C" Q_DECL_EXPORT
int ritual_ZN23QDBusUnixFileDescriptor18takeFileDescriptorEv(
    QDBusUnixFileDescriptor *self) {
  return self->takeFileDescriptor();
}

//  bool QDBusUnixFileDescriptor::isSupported()
extern "C" Q_DECL_EXPORT
bool ritual_ZN23QDBusUnixFileDescriptor11isSupportedEv() {
  return QDBusUnixFileDescriptor::isSupported();
}

#endif  // !defined(QT_NO_DBUS)
