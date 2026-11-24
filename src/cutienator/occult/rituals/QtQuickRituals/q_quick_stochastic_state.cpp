//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickspriteengine_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/qtquickglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#if QT_CONFIG(quick_sprite)
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickspriteengine_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qlist.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>

//  const QMetaObject *QQuickStochasticState::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK21QQuickStochasticState10metaObjectEv(
    const QQuickStochasticState *self) {
  return self->metaObject();
}

//  QString QQuickStochasticState::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN21QQuickStochasticState2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickStochasticState::tr(s, c, n));
}

//  QQuickStochasticState::QQuickStochasticState(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickStochasticState *ritual_ZN21QQuickStochasticStateC1EP7QObject(
    QObject *parent) {
  return new QQuickStochasticState(parent);
}

//  int QQuickStochasticState::duration() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QQuickStochasticState8durationEv(
    const QQuickStochasticState *self) {
  return self->duration();
}

//  QString QQuickStochasticState::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK21QQuickStochasticState4nameEv(
    const QQuickStochasticState *self) {
  return new QString(self->name());
}

//  QVariantMap QQuickStochasticState::to() const
extern "C" Q_DECL_EXPORT
QMap<QString, QVariant> *ritual_ZNK21QQuickStochasticState2toEv(
    const QQuickStochasticState *self) {
  return new QMap<QString, QVariant>(self->to());
}

//  int QQuickStochasticState::durationVariation() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QQuickStochasticState17durationVariationEv(
    const QQuickStochasticState *self) {
  return self->durationVariation();
}

//  int QQuickStochasticState::variedDuration() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QQuickStochasticState14variedDurationEv(
    const QQuickStochasticState *self) {
  return self->variedDuration();
}

//  bool QQuickStochasticState::randomStart() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QQuickStochasticState11randomStartEv(
    const QQuickStochasticState *self) {
  return self->randomStart();
}

//  void QQuickStochasticState::setDuration(int arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickStochasticState11setDurationEi(
    QQuickStochasticState *self,
    int arg) {
  self->setDuration(arg);
}

//  void QQuickStochasticState::setName(const QString &arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickStochasticState7setNameERK7QString(
    QQuickStochasticState *self,
    const QString *arg) {
  self->setName(*arg);
}

//  void QQuickStochasticState::setTo(const QVariantMap &arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickStochasticState5setToERK4QMapI7QString8QVariantE(
    QQuickStochasticState *self,
    const QMap<QString, QVariant> *arg) {
  self->setTo(*arg);
}

//  void QQuickStochasticState::setDurationVariation(int arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickStochasticState20setDurationVariationEi(
    QQuickStochasticState *self,
    int arg) {
  self->setDurationVariation(arg);
}

//  void QQuickStochasticState::setRandomStart(bool arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickStochasticState14setRandomStartEb(
    QQuickStochasticState *self,
    bool arg) {
  self->setRandomStart(arg);
}

//  int QQuickStochasticState::variedDuration() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK21QQuickStochasticState14variedDurationEv(
    const QQuickStochasticState *self) {
  return self->QQuickStochasticState::variedDuration();
}

//  QList<QQuickStochasticState *>::QList()
extern "C" Q_DECL_EXPORT
QList<QQuickStochasticState *> *ritual_list_make_QQuickStochasticState_ptr() {
  return new QList<QQuickStochasticState *>();
}

//  void QList<QQuickStochasticState *>::append(const QQuickStochasticState *
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QQuickStochasticState_ptr(
    QList<QQuickStochasticState *> *self,
    QQuickStochasticState *element) {
  self->append(element);
}

//  qsizetype QList<QQuickStochasticState *>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QQuickStochasticState_ptr(
    const QList<QQuickStochasticState *> *self) {
  return self->size();
}

//  const QQuickStochasticState * &QList<QQuickStochasticState
//      *>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QQuickStochasticState *ritual_list_at_QQuickStochasticState_ptr(
    const QList<QQuickStochasticState *> *self,
    long long index) {
  return self->at(index);
}

//  QList<QQuickStochasticState *>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QQuickStochasticState_ptr(
    QList<QQuickStochasticState *> *self) {
  delete self;
}

#endif  // QT_CONFIG(quick_sprite)
