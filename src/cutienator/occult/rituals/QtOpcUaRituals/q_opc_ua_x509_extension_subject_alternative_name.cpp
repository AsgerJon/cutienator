//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpcUa/qopcuax509extensionsubjectalternativename.h, Qt 6.12.0.
//  Edited by hand on 2026-11-25: the include of
//  <QtOpcUa/qtopcua-config.h> before the #if, as it defines
//  QT_CONFIG(gds); the long #if line split in two.
//  Kept as it is when the generator runs again.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtOpcUa/qopcuaglobal.h>
#include <QtOpcUa/qtopcua-config.h>
#if QT_CONFIG(gds) && QT_CONFIG(openssl) \
    && !defined(Q_OS_DARWIN) && !defined(Q_OS_WINRT)
#include <QtOpcUa/QtOpcUa>
#include <QtOpcUa/qopcuax509extensionsubjectalternativename.h>
#include <QtCore/qstring.h>

//  QOpcUaX509ExtensionSubjectAlternativeName::QOpcUaX509ExtensionSubjectAlte
//      rnativeName()
extern "C" Q_DECL_EXPORT
QOpcUaX509ExtensionSubjectAlternativeName *ritual_ZN41QOpcUaX509ExtensionSubjectAlternativeNameC1Ev() {
  return new QOpcUaX509ExtensionSubjectAlternativeName();
}

//  QOpcUaX509ExtensionSubjectAlternativeName::QOpcUaX509ExtensionSubjectAlte
//      rnativeName(const QOpcUaX509ExtensionSubjectAlternativeName &a0)
extern "C" Q_DECL_EXPORT
QOpcUaX509ExtensionSubjectAlternativeName *ritual_ZN41QOpcUaX509ExtensionSubjectAlternativeNameC1ERKS_(
    const QOpcUaX509ExtensionSubjectAlternativeName *a0) {
  return new QOpcUaX509ExtensionSubjectAlternativeName(*a0);
}

//  QOpcUaX509ExtensionSubjectAlternativeName
//      &QOpcUaX509ExtensionSubjectAlternativeName::operator=(const
//      QOpcUaX509ExtensionSubjectAlternativeName &a0)
extern "C" Q_DECL_EXPORT
QOpcUaX509ExtensionSubjectAlternativeName *ritual_ZN41QOpcUaX509ExtensionSubjectAlternativeNameaSERKS_(
    QOpcUaX509ExtensionSubjectAlternativeName *self,
    const QOpcUaX509ExtensionSubjectAlternativeName *a0) {
  return &(self->operator=(*a0));
}

//  bool QOpcUaX509ExtensionSubjectAlternativeName::operator==(const
//      QOpcUaX509ExtensionSubjectAlternativeName &rhs) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK41QOpcUaX509ExtensionSubjectAlternativeNameeqERKS_(
    const QOpcUaX509ExtensionSubjectAlternativeName *self,
    const QOpcUaX509ExtensionSubjectAlternativeName *rhs) {
  return self->operator==(*rhs);
}

//  QOpcUaX509ExtensionSubjectAlternativeName::~QOpcUaX509ExtensionSubjectAlt
//      ernativeName()
extern "C" Q_DECL_EXPORT
void ritual_ZN41QOpcUaX509ExtensionSubjectAlternativeNameD1Ev(
    QOpcUaX509ExtensionSubjectAlternativeName *self) {
  delete self;
}

//  void QOpcUaX509ExtensionSubjectAlternativeName::addEntry(Type type, const
//      QString &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN41QOpcUaX509ExtensionSubjectAlternativeName8addEntryENS_4TypeERK7QString(
    QOpcUaX509ExtensionSubjectAlternativeName *self,
    QOpcUaX509ExtensionSubjectAlternativeName::Type type,
    const QString *value) {
  self->addEntry(type, *value);
}

//  const QList<std::pair<Type, QString>>
//      &QOpcUaX509ExtensionSubjectAlternativeName::entries() const
extern "C" Q_DECL_EXPORT
const QList<std::pair<QOpcUaX509ExtensionSubjectAlternativeName::Type, QString>> *ritual_ZNK41QOpcUaX509ExtensionSubjectAlternativeName7entriesEv(
    const QOpcUaX509ExtensionSubjectAlternativeName *self) {
  return &(self->entries());
}

#endif  // QT_CONFIG(gds) && QT_CONFIG(openssl) && !defined(Q_OS_DARWIN) && !defined(Q_OS_WINRT)
