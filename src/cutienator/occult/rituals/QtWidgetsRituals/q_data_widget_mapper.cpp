//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qdatawidgetmapper.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qdatawidgetmapper.h>
#include <QtCore/qstring.h>
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/qbytearray.h>

//  const QMetaObject *QDataWidgetMapper::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QDataWidgetMapper10metaObjectEv(
    const QDataWidgetMapper *self) {
  return self->metaObject();
}

//  QString QDataWidgetMapper::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QDataWidgetMapper2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QDataWidgetMapper::tr(s, c, n));
}

//  QDataWidgetMapper::QDataWidgetMapper(QObject *parent)
extern "C" Q_DECL_EXPORT
QDataWidgetMapper *ritual_ZN17QDataWidgetMapperC1EP7QObject(
    QObject *parent) {
  return new QDataWidgetMapper(parent);
}

//  QDataWidgetMapper::~QDataWidgetMapper()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDataWidgetMapperD1Ev(QDataWidgetMapper *self) {
  delete self;
}

//  void QDataWidgetMapper::setModel(QAbstractItemModel *model)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDataWidgetMapper8setModelEP18QAbstractItemModel(
    QDataWidgetMapper *self,
    QAbstractItemModel *model) {
  self->setModel(model);
}

//  QAbstractItemModel *QDataWidgetMapper::model() const
extern "C" Q_DECL_EXPORT
QAbstractItemModel *ritual_ZNK17QDataWidgetMapper5modelEv(
    const QDataWidgetMapper *self) {
  return self->model();
}

//  void QDataWidgetMapper::setItemDelegate(QAbstractItemDelegate *delegate)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDataWidgetMapper15setItemDelegateEP21QAbstractItemDelegate(
    QDataWidgetMapper *self,
    QAbstractItemDelegate *delegate) {
  self->setItemDelegate(delegate);
}

//  QAbstractItemDelegate *QDataWidgetMapper::itemDelegate() const
extern "C" Q_DECL_EXPORT
QAbstractItemDelegate *ritual_ZNK17QDataWidgetMapper12itemDelegateEv(
    const QDataWidgetMapper *self) {
  return self->itemDelegate();
}

//  void QDataWidgetMapper::setRootIndex(const QModelIndex &index)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDataWidgetMapper12setRootIndexERK11QModelIndex(
    QDataWidgetMapper *self,
    const QModelIndex *index) {
  self->setRootIndex(*index);
}

//  QModelIndex QDataWidgetMapper::rootIndex() const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK17QDataWidgetMapper9rootIndexEv(
    const QDataWidgetMapper *self) {
  return new QModelIndex(self->rootIndex());
}

//  void QDataWidgetMapper::setOrientation(Qt::Orientation aOrientation)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDataWidgetMapper14setOrientationEN2Qt11OrientationE(
    QDataWidgetMapper *self,
    Qt::Orientation aOrientation) {
  self->setOrientation(aOrientation);
}

//  Qt::Orientation QDataWidgetMapper::orientation() const
extern "C" Q_DECL_EXPORT
Qt::Orientation ritual_ZNK17QDataWidgetMapper11orientationEv(
    const QDataWidgetMapper *self) {
  return self->orientation();
}

//  void QDataWidgetMapper::setSubmitPolicy(SubmitPolicy policy)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDataWidgetMapper15setSubmitPolicyENS_12SubmitPolicyE(
    QDataWidgetMapper *self,
    QDataWidgetMapper::SubmitPolicy policy) {
  self->setSubmitPolicy(policy);
}

//  SubmitPolicy QDataWidgetMapper::submitPolicy() const
extern "C" Q_DECL_EXPORT
QDataWidgetMapper::SubmitPolicy ritual_ZNK17QDataWidgetMapper12submitPolicyEv(
    const QDataWidgetMapper *self) {
  return self->submitPolicy();
}

//  void QDataWidgetMapper::addMapping(QWidget *widget, int section)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDataWidgetMapper10addMappingEP7QWidgeti(
    QDataWidgetMapper *self,
    QWidget *widget,
    int section) {
  self->addMapping(widget, section);
}

//  void QDataWidgetMapper::addMapping(QWidget *widget, int section, const
//      QByteArray &propertyName)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDataWidgetMapper10addMappingEP7QWidgetiRK10QByteArray(
    QDataWidgetMapper *self,
    QWidget *widget,
    int section,
    const QByteArray *propertyName) {
  self->addMapping(widget, section, *propertyName);
}

//  void QDataWidgetMapper::removeMapping(QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDataWidgetMapper13removeMappingEP7QWidget(
    QDataWidgetMapper *self,
    QWidget *widget) {
  self->removeMapping(widget);
}

//  int QDataWidgetMapper::mappedSection(QWidget *widget) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QDataWidgetMapper13mappedSectionEP7QWidget(
    const QDataWidgetMapper *self,
    QWidget *widget) {
  return self->mappedSection(widget);
}

//  QByteArray QDataWidgetMapper::mappedPropertyName(QWidget *widget) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK17QDataWidgetMapper18mappedPropertyNameEP7QWidget(
    const QDataWidgetMapper *self,
    QWidget *widget) {
  return new QByteArray(self->mappedPropertyName(widget));
}

//  QWidget *QDataWidgetMapper::mappedWidgetAt(int section) const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK17QDataWidgetMapper14mappedWidgetAtEi(
    const QDataWidgetMapper *self,
    int section) {
  return self->mappedWidgetAt(section);
}

//  void QDataWidgetMapper::clearMapping()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDataWidgetMapper12clearMappingEv(QDataWidgetMapper *self) {
  self->clearMapping();
}

//  int QDataWidgetMapper::currentIndex() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QDataWidgetMapper12currentIndexEv(
    const QDataWidgetMapper *self) {
  return self->currentIndex();
}

//  void QDataWidgetMapper::revert()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDataWidgetMapper6revertEv(QDataWidgetMapper *self) {
  self->revert();
}

//  bool QDataWidgetMapper::submit()
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QDataWidgetMapper6submitEv(QDataWidgetMapper *self) {
  return self->submit();
}

//  void QDataWidgetMapper::toFirst()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDataWidgetMapper7toFirstEv(QDataWidgetMapper *self) {
  self->toFirst();
}

//  void QDataWidgetMapper::toLast()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDataWidgetMapper6toLastEv(QDataWidgetMapper *self) {
  self->toLast();
}

//  void QDataWidgetMapper::toNext()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDataWidgetMapper6toNextEv(QDataWidgetMapper *self) {
  self->toNext();
}

//  void QDataWidgetMapper::toPrevious()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDataWidgetMapper10toPreviousEv(QDataWidgetMapper *self) {
  self->toPrevious();
}

//  void QDataWidgetMapper::setCurrentIndex(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDataWidgetMapper15setCurrentIndexEi(
    QDataWidgetMapper *self,
    int index) {
  self->setCurrentIndex(index);
}

//  void QDataWidgetMapper::setCurrentModelIndex(const QModelIndex &index)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDataWidgetMapper20setCurrentModelIndexERK11QModelIndex(
    QDataWidgetMapper *self,
    const QModelIndex *index) {
  self->setCurrentModelIndex(*index);
}
