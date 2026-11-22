//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qproperty.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qproperty.h>
#include <QtCore/qstring.h>

//  QPropertyBindingError::QPropertyBindingError()
extern "C" Q_DECL_EXPORT
QPropertyBindingError *ritual_ZN21QPropertyBindingErrorC1Ev() {
  return new QPropertyBindingError();
}

//  QPropertyBindingError::QPropertyBindingError(Type type, const QString
//      &description)
extern "C" Q_DECL_EXPORT
QPropertyBindingError *ritual_ZN21QPropertyBindingErrorC1ENS_4TypeERK7QString(
    QPropertyBindingError::Type type,
    const QString *description) {
  return new QPropertyBindingError(type, *description);
}

//  QPropertyBindingError::QPropertyBindingError(const QPropertyBindingError
//      &other)
extern "C" Q_DECL_EXPORT
QPropertyBindingError *ritual_ZN21QPropertyBindingErrorC1ERKS_(
    const QPropertyBindingError *other) {
  return new QPropertyBindingError(*other);
}

//  QPropertyBindingError::~QPropertyBindingError()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QPropertyBindingErrorD1Ev(QPropertyBindingError *self) {
  delete self;
}

//  bool QPropertyBindingError::hasError() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QPropertyBindingError8hasErrorEv(
    const QPropertyBindingError *self) {
  return self->hasError();
}

//  Type QPropertyBindingError::type() const
extern "C" Q_DECL_EXPORT
QPropertyBindingError::Type ritual_ZNK21QPropertyBindingError4typeEv(
    const QPropertyBindingError *self) {
  return self->type();
}

//  QString QPropertyBindingError::description() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK21QPropertyBindingError11descriptionEv(
    const QPropertyBindingError *self) {
  return new QString(self->description());
}
