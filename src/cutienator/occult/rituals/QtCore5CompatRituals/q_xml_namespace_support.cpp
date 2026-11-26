//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore5Compat/qxml.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore5Compat/qxml.h>
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>

//  QXmlNamespaceSupport::QXmlNamespaceSupport()
extern "C" Q_DECL_EXPORT
QXmlNamespaceSupport *ritual_ZN20QXmlNamespaceSupportC1Ev() {
  return new QXmlNamespaceSupport();
}

//  QXmlNamespaceSupport::~QXmlNamespaceSupport()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QXmlNamespaceSupportD1Ev(QXmlNamespaceSupport *self) {
  delete self;
}

//  void QXmlNamespaceSupport::setPrefix(const QString &a0, const QString
//      &a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QXmlNamespaceSupport9setPrefixERK7QStringS2_(
    QXmlNamespaceSupport *self,
    const QString *a0,
    const QString *a1) {
  self->setPrefix(*a0, *a1);
}

//  QString QXmlNamespaceSupport::prefix(const QString &a0) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK20QXmlNamespaceSupport6prefixERK7QString(
    const QXmlNamespaceSupport *self,
    const QString *a0) {
  return new QString(self->prefix(*a0));
}

//  QString QXmlNamespaceSupport::uri(const QString &a0) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK20QXmlNamespaceSupport3uriERK7QString(
    const QXmlNamespaceSupport *self,
    const QString *a0) {
  return new QString(self->uri(*a0));
}

//  void QXmlNamespaceSupport::splitName(const QString &a0, QString &a1,
//      QString &a2) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK20QXmlNamespaceSupport9splitNameERK7QStringRS0_S3_(
    const QXmlNamespaceSupport *self,
    const QString *a0,
    QString *a1,
    QString *a2) {
  self->splitName(*a0, *a1, *a2);
}

//  void QXmlNamespaceSupport::processName(const QString &a0, bool a1,
//      QString &a2, QString &a3) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK20QXmlNamespaceSupport11processNameERK7QStringbRS0_S3_(
    const QXmlNamespaceSupport *self,
    const QString *a0,
    bool a1,
    QString *a2,
    QString *a3) {
  self->processName(*a0, a1, *a2, *a3);
}

//  QStringList QXmlNamespaceSupport::prefixes() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK20QXmlNamespaceSupport8prefixesEv(
    const QXmlNamespaceSupport *self) {
  return new QList<QString>(self->prefixes());
}

//  QStringList QXmlNamespaceSupport::prefixes(const QString &a0) const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK20QXmlNamespaceSupport8prefixesERK7QString(
    const QXmlNamespaceSupport *self,
    const QString *a0) {
  return new QList<QString>(self->prefixes(*a0));
}

//  void QXmlNamespaceSupport::pushContext()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QXmlNamespaceSupport11pushContextEv(
    QXmlNamespaceSupport *self) {
  self->pushContext();
}

//  void QXmlNamespaceSupport::popContext()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QXmlNamespaceSupport10popContextEv(
    QXmlNamespaceSupport *self) {
  self->popContext();
}

//  void QXmlNamespaceSupport::reset()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QXmlNamespaceSupport5resetEv(QXmlNamespaceSupport *self) {
  self->reset();
}
