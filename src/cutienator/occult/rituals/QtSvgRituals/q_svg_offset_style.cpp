//  Written by dev_tooling.RitualGenerator from the records of
//  QtSvg/6.12.0/QtSvg/private/qsvgstyle_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtSvg/6.12.0/QtSvg/private/qtsvgglobal_p.h>
#include <QtSvg/QtSvg>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSvg/6.12.0/QtSvg/private/qsvgstyle_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qpainterpath.h>
#include <cstring>

//  A QSvgOffsetStyle that Python can take functions over in. Every QSvgOffsetStyle
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQSvgOffsetStyleCall0)(const void *, int *);
typedef bool (*CuteQSvgOffsetStyleCall1)(const void *, int *);
class CuteQSvgOffsetStyle : public QSvgOffsetStyle {
public:
  using QSvgOffsetStyle::QSvgOffsetStyle;
  CuteQSvgOffsetStyle(const QSvgOffsetStyle &other) : QSvgOffsetStyle(other) {}
  void *taken[2] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK17QSvgStyleProperty4typeEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QSvgStyleProperty9isDefaultEv")) {
      taken[1] = call;
      return true;
    }
    return false;
  }

  //  Type QSvgOffsetStyle::type() const
  QSvgStyleProperty::Type type() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQSvgOffsetStyleCall0 call = reinterpret_cast<CuteQSvgOffsetStyleCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return static_cast<QSvgStyleProperty::Type>(given);
    }
    return QSvgOffsetStyle::type();
  }

  //  bool QSvgStyleProperty::isDefault() const
  bool isDefault() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQSvgOffsetStyleCall1 call = reinterpret_cast<CuteQSvgOffsetStyleCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSvgStyleProperty::isDefault();
  }
};

//  QSvgOffsetStyle::QSvgOffsetStyle()
extern "C" Q_DECL_EXPORT
QSvgOffsetStyle *ritual_ZN15QSvgOffsetStyleC1Ev() {
  return new CuteQSvgOffsetStyle();
}

//  QSvgOffsetStyle::~QSvgOffsetStyle()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QSvgOffsetStyleD1Ev(QSvgOffsetStyle *self) {
  delete self;
}

//  Type QSvgOffsetStyle::type() const
extern "C" Q_DECL_EXPORT
QSvgStyleProperty::Type ritual_ZNK15QSvgOffsetStyle4typeEv(
    const QSvgOffsetStyle *self) {
  return self->type();
}

//  void QSvgOffsetStyle::setPath(const QPainterPath &path)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QSvgOffsetStyle7setPathERK12QPainterPath(
    QSvgOffsetStyle *self,
    const QPainterPath *path) {
  self->setPath(*path);
}

//  const QPainterPath &QSvgOffsetStyle::path() const
extern "C" Q_DECL_EXPORT
QPainterPath *ritual_ZNK15QSvgOffsetStyle4pathEv(
    const QSvgOffsetStyle *self) {
  return new QPainterPath(self->path());
}

//  void QSvgOffsetStyle::setRotateAngle(qreal angle)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QSvgOffsetStyle14setRotateAngleEd(
    QSvgOffsetStyle *self,
    qreal angle) {
  self->setRotateAngle(angle);
}

//  qreal QSvgOffsetStyle::rotateAngle() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK15QSvgOffsetStyle11rotateAngleEv(
    const QSvgOffsetStyle *self) {
  return self->rotateAngle();
}

//  void QSvgOffsetStyle::setRotateType(QtSvg::OffsetRotateType type)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QSvgOffsetStyle13setRotateTypeEN5QtSvg16OffsetRotateTypeE(
    QSvgOffsetStyle *self,
    QtSvg::OffsetRotateType type) {
  self->setRotateType(type);
}

//  QtSvg::OffsetRotateType QSvgOffsetStyle::rotateType() const
extern "C" Q_DECL_EXPORT
QtSvg::OffsetRotateType ritual_ZNK15QSvgOffsetStyle10rotateTypeEv(
    const QSvgOffsetStyle *self) {
  return self->rotateType();
}

//  void QSvgOffsetStyle::setDistance(qreal distance)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QSvgOffsetStyle11setDistanceEd(
    QSvgOffsetStyle *self,
    qreal distance) {
  self->setDistance(distance);
}

//  qreal QSvgOffsetStyle::distance() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK15QSvgOffsetStyle8distanceEv(const QSvgOffsetStyle *self) {
  return self->distance();
}

//  a Python function taken by a CuteQSvgOffsetStyle, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSvgOffsetStyle(
    QSvgOffsetStyle *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSvgOffsetStyle *>(self)->take(key, call);
}

//  Type QSvgOffsetStyle::type() const
extern "C" Q_DECL_EXPORT
QSvgStyleProperty::Type ritual_own_ZNK15QSvgOffsetStyle4typeEv(
    const QSvgOffsetStyle *self) {
  return self->QSvgOffsetStyle::type();
}
