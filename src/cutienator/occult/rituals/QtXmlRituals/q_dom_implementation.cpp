//  Written by dev_tooling.RitualGenerator from the records of QtXml/qdom.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtXml/qtxmlglobal.h>
#if QT_CONFIG(dom)
#include <QtXml/qdom.h>
#include <QtCore/qstring.h>

//  QDomImplementation::QDomImplementation()
extern "C" Q_DECL_EXPORT
QDomImplementation *ritual_ZN18QDomImplementationC1Ev() {
  return new QDomImplementation();
}

//  QDomImplementation::QDomImplementation(const QDomImplementation
//      &implementation)
extern "C" Q_DECL_EXPORT
QDomImplementation *ritual_ZN18QDomImplementationC1ERKS_(
    const QDomImplementation *implementation) {
  return new QDomImplementation(*implementation);
}

//  QDomImplementation::~QDomImplementation()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QDomImplementationD1Ev(QDomImplementation *self) {
  delete self;
}

//  bool QDomImplementation::operator==(const QDomImplementation &other)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QDomImplementationeqERKS_(
    const QDomImplementation *self,
    const QDomImplementation *other) {
  return self->operator==(*other);
}

//  bool QDomImplementation::operator!=(const QDomImplementation &other)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QDomImplementationneERKS_(
    const QDomImplementation *self,
    const QDomImplementation *other) {
  return self->operator!=(*other);
}

//  bool QDomImplementation::hasFeature(const QString &feature, const QString
//      &version) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QDomImplementation10hasFeatureERK7QStringS2_(
    const QDomImplementation *self,
    const QString *feature,
    const QString *version) {
  return self->hasFeature(*feature, *version);
}

//  QDomDocumentType QDomImplementation::createDocumentType(const QString
//      &qName, const QString &publicId, const QString &systemId)
extern "C" Q_DECL_EXPORT
QDomDocumentType *ritual_ZN18QDomImplementation18createDocumentTypeERK7QStringS2_S2_(
    QDomImplementation *self,
    const QString *qName,
    const QString *publicId,
    const QString *systemId) {
  return new QDomDocumentType(
      self->createDocumentType(
          *qName,
          *publicId,
          *systemId));
}

//  QDomDocument QDomImplementation::createDocument(const QString &nsURI,
//      const QString &qName, const QDomDocumentType &doctype)
extern "C" Q_DECL_EXPORT
QDomDocument *ritual_ZN18QDomImplementation14createDocumentERK7QStringS2_RK16QDomDocumentType(
    QDomImplementation *self,
    const QString *nsURI,
    const QString *qName,
    const QDomDocumentType *doctype) {
  return new QDomDocument(self->createDocument(*nsURI, *qName, *doctype));
}

//  InvalidDataPolicy QDomImplementation::invalidDataPolicy()
extern "C" Q_DECL_EXPORT
QDomImplementation::InvalidDataPolicy ritual_ZN18QDomImplementation17invalidDataPolicyEv() {
  return QDomImplementation::invalidDataPolicy();
}

//  void QDomImplementation::setInvalidDataPolicy(InvalidDataPolicy policy)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QDomImplementation20setInvalidDataPolicyENS_17InvalidDataPolicyE(
    QDomImplementation::InvalidDataPolicy policy) {
  QDomImplementation::setInvalidDataPolicy(policy);
}

//  bool QDomImplementation::isNull()
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QDomImplementation6isNullEv(QDomImplementation *self) {
  return self->isNull();
}

//  QDomImplementation::QDomImplementation(QDomImplementationPrivate *a0)
extern "C" Q_DECL_EXPORT
QDomImplementation *ritual_ZN18QDomImplementationC1EP25QDomImplementationPrivate(
    QDomImplementationPrivate *a0) {
  return new QDomImplementation(a0);
}

#endif  // QT_CONFIG(dom)
