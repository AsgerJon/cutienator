//  Written by dev_tooling.RitualGenerator from the records of
//  QtSvg/6.12.0/QtSvg/private/qsvgcssproperties_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtSvg/qtsvgglobal.h>
#include <QtSvg/6.12.0/QtSvg/private/qtsvgglobal_p.h>
#if QT_CONFIG(cssparser)
#include <QtSvg/6.12.0/QtSvg/private/qtsvgglobal_p.h>
#include <QtSvg/QtSvg>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSvg/6.12.0/QtSvg/private/qsvgcssproperties_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qlist.h>

//  QSvgAnimationProperty::~QSvgAnimationProperty()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSvgAnimationPropertyD1Ev(QSvgAnimationProperty *self) {
  delete self;
}

//  QList<QSvgAnimationProperty>::QList()
extern "C" Q_DECL_EXPORT
QList<QSvgAnimationProperty> *ritual_list_make_QSvgAnimationProperty() {
  return new QList<QSvgAnimationProperty>();
}

//  void QList<QSvgAnimationProperty>::append(const QSvgAnimationProperty
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QSvgAnimationProperty(
    QList<QSvgAnimationProperty> *self,
    const QSvgAnimationProperty *element) {
  self->append(*element);
}

//  qsizetype QList<QSvgAnimationProperty>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QSvgAnimationProperty(
    const QList<QSvgAnimationProperty> *self) {
  return self->size();
}

//  const QSvgAnimationProperty &QList<QSvgAnimationProperty>::at(qsizetype
//      i) const
extern "C" Q_DECL_EXPORT
QSvgAnimationProperty *ritual_list_at_QSvgAnimationProperty(
    const QList<QSvgAnimationProperty> *self,
    long long index) {
  return new QSvgAnimationProperty(self->at(index));
}

//  QList<QSvgAnimationProperty>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QSvgAnimationProperty(
    QList<QSvgAnimationProperty> *self) {
  delete self;
}

#endif  // QT_CONFIG(cssparser)
