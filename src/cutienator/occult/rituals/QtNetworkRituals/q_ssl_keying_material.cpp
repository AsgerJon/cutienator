//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/qsslkeyingmaterial.h, Qt 6.12.0. Changes made here are lost.
#include <QtNetwork/qtnetworkglobal.h>
#if QT_CONFIG(ssl)
#if QT_CONFIG(ssl)
#include <QtNetwork/qsslkeyingmaterial.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qdebug.h>
#include <QtCore/qlist.h>

//  QSslKeyingMaterial::QSslKeyingMaterial()
extern "C" Q_DECL_EXPORT
QSslKeyingMaterial *ritual_ZN18QSslKeyingMaterialC1Ev() {
  return new QSslKeyingMaterial();
}

//  QSslKeyingMaterial::QSslKeyingMaterial(const QByteArray &label, qsizetype
//      size)
extern "C" Q_DECL_EXPORT
QSslKeyingMaterial *ritual_ZN18QSslKeyingMaterialC1ERK10QByteArrayx(
    const QByteArray *label,
    qsizetype size) {
  return new QSslKeyingMaterial(*label, size);
}

//  QSslKeyingMaterial::QSslKeyingMaterial(const QByteArray &label, qsizetype
//      size, const QByteArray &context)
extern "C" Q_DECL_EXPORT
QSslKeyingMaterial *ritual_ZN18QSslKeyingMaterialC1ERK10QByteArrayxS2_(
    const QByteArray *label,
    qsizetype size,
    const QByteArray *context) {
  return new QSslKeyingMaterial(*label, size, *context);
}

//  QSslKeyingMaterial::QSslKeyingMaterial(const QSslKeyingMaterial &other)
extern "C" Q_DECL_EXPORT
QSslKeyingMaterial *ritual_ZN18QSslKeyingMaterialC1ERKS_(
    const QSslKeyingMaterial *other) {
  return new QSslKeyingMaterial(*other);
}

//  QSslKeyingMaterial::~QSslKeyingMaterial()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QSslKeyingMaterialD1Ev(QSslKeyingMaterial *self) {
  delete self;
}

//  bool QSslKeyingMaterial::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QSslKeyingMaterial7isValidEv(
    const QSslKeyingMaterial *self) {
  return self->isValid();
}

//  QByteArray QSslKeyingMaterial::label() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK18QSslKeyingMaterial5labelEv(
    const QSslKeyingMaterial *self) {
  return new QByteArray(self->label());
}

//  QByteArray QSslKeyingMaterial::context() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK18QSslKeyingMaterial7contextEv(
    const QSslKeyingMaterial *self) {
  return new QByteArray(self->context());
}

//  QByteArray QSslKeyingMaterial::value() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK18QSslKeyingMaterial5valueEv(
    const QSslKeyingMaterial *self) {
  return new QByteArray(self->value());
}

//  qsizetype QSslKeyingMaterial::requestedSize() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK18QSslKeyingMaterial13requestedSizeEv(
    const QSslKeyingMaterial *self) {
  return self->requestedSize();
}

//  QSslKeyingMaterial QSslKeyingMaterial::clone() const
extern "C" Q_DECL_EXPORT
QSslKeyingMaterial *ritual_ZNK18QSslKeyingMaterial5cloneEv(
    const QSslKeyingMaterial *self) {
  return new QSslKeyingMaterial(self->clone());
}

//  bool operator==(const QSslKeyingMaterial &lhs, const QSslKeyingMaterial
//      &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK18QSslKeyingMaterialS1_(
    const QSslKeyingMaterial *lhs,
    const QSslKeyingMaterial *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QSslKeyingMaterial &lhs, const QSslKeyingMaterial
//      &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK18QSslKeyingMaterialS1_(
    const QSslKeyingMaterial *lhs,
    const QSslKeyingMaterial *rhs) {
  return operator!=(*lhs, *rhs);
}

#if !defined(QT_NO_DEBUG_STREAM)
//  QDebug operator<<(QDebug debug, const QSslKeyingMaterial &keying)
extern "C" Q_DECL_EXPORT
QDebug *ritual_Zls6QDebugRK18QSslKeyingMaterial(
    const QDebug *debug,
    const QSslKeyingMaterial *keying) {
  return new QDebug(operator<<(*debug, *keying));
}
#endif  // !defined(QT_NO_DEBUG_STREAM)

//  QList<QSslKeyingMaterial>::QList()
extern "C" Q_DECL_EXPORT
QList<QSslKeyingMaterial> *ritual_list_make_QSslKeyingMaterial() {
  return new QList<QSslKeyingMaterial>();
}

//  void QList<QSslKeyingMaterial>::append(const QSslKeyingMaterial &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QSslKeyingMaterial(
    QList<QSslKeyingMaterial> *self,
    const QSslKeyingMaterial *element) {
  self->append(*element);
}

//  qsizetype QList<QSslKeyingMaterial>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QSslKeyingMaterial(
    const QList<QSslKeyingMaterial> *self) {
  return self->size();
}

//  const QSslKeyingMaterial &QList<QSslKeyingMaterial>::at(qsizetype i)
//      const
extern "C" Q_DECL_EXPORT
QSslKeyingMaterial *ritual_list_at_QSslKeyingMaterial(
    const QList<QSslKeyingMaterial> *self,
    long long index) {
  return new QSslKeyingMaterial(self->at(index));
}

//  QList<QSslKeyingMaterial>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QSslKeyingMaterial(QList<QSslKeyingMaterial> *self) {
  delete self;
}

#endif  // QT_CONFIG(ssl)
#endif  // QT_CONFIG(ssl)
