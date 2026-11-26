//  Written by dev_tooling.RitualGenerator from the records of QtQuickDialogs
//  2Utils/6.12.0/QtQuickDialogs2Utils/private/qquickfilenamefilter_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuickDialogs2Utils/6.12.0/QtQuickDialogs2Utils/private/qtquickdialogs2utilsglobal_p.h>
#include <QtQuickDialogs2Utils/QtQuickDialogs2Utils>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickDialogs2Utils/6.12.0/QtQuickDialogs2Utils/private/qquickfilenamefilter_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>
#include <QtCore/QSharedPointer>

//  const QMetaObject *QQuickFileNameFilter::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK20QQuickFileNameFilter10metaObjectEv(
    const QQuickFileNameFilter *self) {
  return self->metaObject();
}

//  void *QQuickFileNameFilter::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN20QQuickFileNameFilter11qt_metacastEPKc(
    QQuickFileNameFilter *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickFileNameFilter::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN20QQuickFileNameFilter11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickFileNameFilter *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickFileNameFilter::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN20QQuickFileNameFilter2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickFileNameFilter::tr(s, c, n));
}

//  QQuickFileNameFilter::QQuickFileNameFilter(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickFileNameFilter *ritual_ZN20QQuickFileNameFilterC1EP7QObject(
    QObject *parent) {
  return new QQuickFileNameFilter(parent);
}

//  int QQuickFileNameFilter::index() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QQuickFileNameFilter5indexEv(
    const QQuickFileNameFilter *self) {
  return self->index();
}

//  void QQuickFileNameFilter::setIndex(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickFileNameFilter8setIndexEi(
    QQuickFileNameFilter *self,
    int index) {
  self->setIndex(index);
}

//  QString QQuickFileNameFilter::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK20QQuickFileNameFilter4nameEv(
    const QQuickFileNameFilter *self) {
  return new QString(self->name());
}

//  QStringList QQuickFileNameFilter::extensions() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK20QQuickFileNameFilter10extensionsEv(
    const QQuickFileNameFilter *self) {
  return new QList<QString>(self->extensions());
}

//  QStringList QQuickFileNameFilter::globs() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK20QQuickFileNameFilter5globsEv(
    const QQuickFileNameFilter *self) {
  return new QList<QString>(self->globs());
}

//  QSharedPointer<QFileDialogOptions> QQuickFileNameFilter::options() const
extern "C" Q_DECL_EXPORT
QSharedPointer<QFileDialogOptions> *ritual_ZNK20QQuickFileNameFilter7optionsEv(
    const QQuickFileNameFilter *self) {
  return new QSharedPointer<QFileDialogOptions>(self->options());
}

//  void QQuickFileNameFilter::setOptions(const
//      QSharedPointer<QFileDialogOptions> &options)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickFileNameFilter10setOptionsERK14QSharedPointerI18QFileDialogOptionsE(
    QQuickFileNameFilter *self,
    const QSharedPointer<QFileDialogOptions> *options) {
  self->setOptions(*options);
}

//  void QQuickFileNameFilter::update(const QString &filter)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickFileNameFilter6updateERK7QString(
    QQuickFileNameFilter *self,
    const QString *filter) {
  self->update(*filter);
}

//  void QQuickFileNameFilter::indexChanged(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickFileNameFilter12indexChangedEi(
    QQuickFileNameFilter *self,
    int index) {
  self->indexChanged(index);
}

//  void QQuickFileNameFilter::nameChanged(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickFileNameFilter11nameChangedERK7QString(
    QQuickFileNameFilter *self,
    const QString *name) {
  self->nameChanged(*name);
}

//  void QQuickFileNameFilter::extensionsChanged(const QStringList
//      &extensions)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickFileNameFilter17extensionsChangedERK5QListI7QStringE(
    QQuickFileNameFilter *self,
    const QList<QString> *extensions) {
  self->extensionsChanged(*extensions);
}

//  void QQuickFileNameFilter::globsChanged(const QStringList &globs)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickFileNameFilter12globsChangedERK5QListI7QStringE(
    QQuickFileNameFilter *self,
    const QList<QString> *globs) {
  self->globsChanged(*globs);
}

//  QStringList QQuickFileNameFilter::nameFilters() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK20QQuickFileNameFilter11nameFiltersEv(
    const QQuickFileNameFilter *self) {
  return new QList<QString>(self->nameFilters());
}

//  QString QQuickFileNameFilter::nameFilter(int index) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK20QQuickFileNameFilter10nameFilterEi(
    const QQuickFileNameFilter *self,
    int index) {
  return new QString(self->nameFilter(index));
}

//  a QSharedPointer<QFileDialogOptions> a ritual of QQuickFileNameFilter
//      gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQuickFileNameFilter__QSharedPointer_QFileDialogOptions(
    QSharedPointer<QFileDialogOptions> *self) {
  delete self;
}
