//  Written by dev_tooling.RitualGenerator from the records of
//  QtHelp/qcompressedhelpinfo.h, Qt 6.12.0. Changes made here are lost.
#include <QtHelp/qcompressedhelpinfo.h>
#include <QtCore/qstring.h>
#include <QtCore/qversionnumber.h>

//  QCompressedHelpInfo::QCompressedHelpInfo()
extern "C" Q_DECL_EXPORT
QCompressedHelpInfo *ritual_ZN19QCompressedHelpInfoC1Ev() {
  return new QCompressedHelpInfo();
}

//  QCompressedHelpInfo::QCompressedHelpInfo(const QCompressedHelpInfo
//      &other)
extern "C" Q_DECL_EXPORT
QCompressedHelpInfo *ritual_ZN19QCompressedHelpInfoC1ERKS_(
    const QCompressedHelpInfo *other) {
  return new QCompressedHelpInfo(*other);
}

//  QCompressedHelpInfo::QCompressedHelpInfo(QCompressedHelpInfo &&other)
extern "C" Q_DECL_EXPORT
QCompressedHelpInfo *ritual_ZN19QCompressedHelpInfoC1EOS_(
    QCompressedHelpInfo *other) {
  return new QCompressedHelpInfo(std::move(*other));
}

//  QCompressedHelpInfo::~QCompressedHelpInfo()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QCompressedHelpInfoD1Ev(QCompressedHelpInfo *self) {
  delete self;
}

//  QCompressedHelpInfo &QCompressedHelpInfo::operator=(const
//      QCompressedHelpInfo &other)
extern "C" Q_DECL_EXPORT
QCompressedHelpInfo *ritual_ZN19QCompressedHelpInfoaSERKS_(
    QCompressedHelpInfo *self,
    const QCompressedHelpInfo *other) {
  return &(self->operator=(*other));
}

//  QCompressedHelpInfo &QCompressedHelpInfo::operator=(QCompressedHelpInfo
//      &&other)
extern "C" Q_DECL_EXPORT
QCompressedHelpInfo *ritual_ZN19QCompressedHelpInfoaSEOS_(
    QCompressedHelpInfo *self,
    QCompressedHelpInfo *other) {
  return &(self->operator=(std::move(*other)));
}

//  void QCompressedHelpInfo::swap(QCompressedHelpInfo &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QCompressedHelpInfo4swapERS_(
    QCompressedHelpInfo *self,
    QCompressedHelpInfo *other) {
  self->swap(*other);
}

//  QString QCompressedHelpInfo::namespaceName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QCompressedHelpInfo13namespaceNameEv(
    const QCompressedHelpInfo *self) {
  return new QString(self->namespaceName());
}

//  QString QCompressedHelpInfo::component() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QCompressedHelpInfo9componentEv(
    const QCompressedHelpInfo *self) {
  return new QString(self->component());
}

//  QVersionNumber QCompressedHelpInfo::version() const
extern "C" Q_DECL_EXPORT
QVersionNumber *ritual_ZNK19QCompressedHelpInfo7versionEv(
    const QCompressedHelpInfo *self) {
  return new QVersionNumber(self->version());
}

//  bool QCompressedHelpInfo::isNull() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QCompressedHelpInfo6isNullEv(
    const QCompressedHelpInfo *self) {
  return self->isNull();
}

//  QCompressedHelpInfo QCompressedHelpInfo::fromCompressedHelpFile(const
//      QString &documentationFileName)
extern "C" Q_DECL_EXPORT
QCompressedHelpInfo *ritual_ZN19QCompressedHelpInfo22fromCompressedHelpFileERK7QString(
    const QString *documentationFileName) {
  return new QCompressedHelpInfo(
      QCompressedHelpInfo::fromCompressedHelpFile(
          *documentationFileName));
}
