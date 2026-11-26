//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/actionrepository_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/actionrepository_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qabstractitemmodel.h>
#include <QtWidgets/qwidget.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/qdesigner_utils_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qicon.h>
#include <QtCore/qlist.h>

//  const QMetaObject *qdesigner_internal::ActionModel::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18qdesigner_internal11ActionModel10metaObjectEv(
    const qdesigner_internal::ActionModel *self) {
  return self->metaObject();
}

//  void *qdesigner_internal::ActionModel::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN18qdesigner_internal11ActionModel11qt_metacastEPKc(
    qdesigner_internal::ActionModel *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int qdesigner_internal::ActionModel::qt_metacall(QMetaObject::Call a0,
//      int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN18qdesigner_internal11ActionModel11qt_metacallEN11QMetaObject4CallEiPPv(
    qdesigner_internal::ActionModel *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString qdesigner_internal::ActionModel::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18qdesigner_internal11ActionModel2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(qdesigner_internal::ActionModel::tr(s, c, n));
}

//  qdesigner_internal::ActionModel::ActionModel(QWidget *parent)
extern "C" Q_DECL_EXPORT
qdesigner_internal::ActionModel *ritual_ZN18qdesigner_internal11ActionModelC1EP7QWidget(
    QWidget *parent) {
  return new qdesigner_internal::ActionModel(parent);
}

//  void
//      qdesigner_internal::ActionModel::initialize(QDesignerFormEditorInterf
//      ace *core)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal11ActionModel10initializeEP28QDesignerFormEditorInterface(
    qdesigner_internal::ActionModel *self,
    QDesignerFormEditorInterface *core) {
  self->initialize(core);
}

//  void qdesigner_internal::ActionModel::clearActions()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal11ActionModel12clearActionsEv(
    qdesigner_internal::ActionModel *self) {
  self->clearActions();
}

//  QModelIndex qdesigner_internal::ActionModel::addAction(QAction *a)
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZN18qdesigner_internal11ActionModel9addActionEP7QAction(
    qdesigner_internal::ActionModel *self,
    QAction *a) {
  return new QModelIndex(self->addAction(a));
}

//  void qdesigner_internal::ActionModel::remove(int row)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal11ActionModel6removeEi(
    qdesigner_internal::ActionModel *self,
    int row) {
  self->remove(row);
}

//  void qdesigner_internal::ActionModel::update(int row)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal11ActionModel6updateEi(
    qdesigner_internal::ActionModel *self,
    int row) {
  self->update(row);
}

//  int qdesigner_internal::ActionModel::findAction(QAction *a0) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18qdesigner_internal11ActionModel10findActionEP7QAction(
    const qdesigner_internal::ActionModel *self,
    QAction *a0) {
  return self->findAction(a0);
}

//  QString qdesigner_internal::ActionModel::actionName(int row) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18qdesigner_internal11ActionModel10actionNameEi(
    const qdesigner_internal::ActionModel *self,
    int row) {
  return new QString(self->actionName(row));
}

//  QAction *qdesigner_internal::ActionModel::actionAt(const QModelIndex
//      &index) const
extern "C" Q_DECL_EXPORT
QAction *ritual_ZNK18qdesigner_internal11ActionModel8actionAtERK11QModelIndex(
    const qdesigner_internal::ActionModel *self,
    const QModelIndex *index) {
  return self->actionAt(*index);
}

//  QModelIndex qdesigner_internal::ActionModel::indexOf(QAction *a) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK18qdesigner_internal11ActionModel7indexOfEP7QAction(
    const qdesigner_internal::ActionModel *self,
    QAction *a) {
  return new QModelIndex(self->indexOf(a));
}

//  QMimeData *qdesigner_internal::ActionModel::mimeData(const
//      QModelIndexList &indexes) const
extern "C" Q_DECL_EXPORT
QMimeData *ritual_ZNK18qdesigner_internal11ActionModel8mimeDataERK5QListI11QModelIndexE(
    const qdesigner_internal::ActionModel *self,
    const QList<QModelIndex> *indexes) {
  return self->mimeData(*indexes);
}

//  QStringList qdesigner_internal::ActionModel::mimeTypes() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK18qdesigner_internal11ActionModel9mimeTypesEv(
    const qdesigner_internal::ActionModel *self) {
  return new QList<QString>(self->mimeTypes());
}

//  bool qdesigner_internal::ActionModel::dropMimeData(const QMimeData *data,
//      Qt::DropAction action, int row, int column, const QModelIndex
//      &parent)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18qdesigner_internal11ActionModel12dropMimeDataEPK9QMimeDataN2Qt10DropActionEiiRK11QModelIndex(
    qdesigner_internal::ActionModel *self,
    const QMimeData *data,
    Qt::DropAction action,
    int row,
    int column,
    const QModelIndex *parent) {
  return self->dropMimeData(data, action, row, column, *parent);
}

//  QWidgetList qdesigner_internal::ActionModel::associatedWidgets(const
//      QAction *action)
extern "C" Q_DECL_EXPORT
QList<QWidget *> *ritual_ZN18qdesigner_internal11ActionModel17associatedWidgetsEPK7QAction(
    const QAction *action) {
  return new QList<QWidget *>(
      qdesigner_internal::ActionModel::associatedWidgets(
          action));
}

//  PropertySheetKeySequenceValue qdesigner_internal::ActionModel::actionShor
//      tCut(QDesignerFormEditorInterface *core, QAction *action)
extern "C" Q_DECL_EXPORT
qdesigner_internal::PropertySheetKeySequenceValue *ritual_ZN18qdesigner_internal11ActionModel14actionShortCutEP28QDesignerFormEditorInterfaceP7QAction(
    QDesignerFormEditorInterface *core,
    QAction *action) {
  return new qdesigner_internal::PropertySheetKeySequenceValue(
      qdesigner_internal::ActionModel::actionShortCut(
          core,
          action));
}

//  PropertySheetKeySequenceValue
//      qdesigner_internal::ActionModel::actionShortCut(const
//      QDesignerPropertySheetExtension *ps)
extern "C" Q_DECL_EXPORT
qdesigner_internal::PropertySheetKeySequenceValue *ritual_ZN18qdesigner_internal11ActionModel14actionShortCutEPK31QDesignerPropertySheetExtension(
    const QDesignerPropertySheetExtension *ps) {
  return new qdesigner_internal::PropertySheetKeySequenceValue(
      qdesigner_internal::ActionModel::actionShortCut(
          ps));
}

//  void qdesigner_internal::ActionModel::resourceImageDropped(const QString
//      &path, QAction *action)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal11ActionModel20resourceImageDroppedERK7QStringP7QAction(
    qdesigner_internal::ActionModel *self,
    const QString *path,
    QAction *action) {
  self->resourceImageDropped(*path, action);
}

//  void
//      qdesigner_internal::ActionModel::setItems(QDesignerFormEditorInterfac
//      e *core, QAction *a, const QIcon &defaultIcon, QStandardItemList &sl)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal11ActionModel8setItemsEP28QDesignerFormEditorInterfaceP7QActionRK5QIconR5QListIP13QStandardItemE(
    QDesignerFormEditorInterface *core,
    QAction *a,
    const QIcon *defaultIcon,
    qdesigner_internal::ActionModel::QStandardItemList *sl) {
  qdesigner_internal::ActionModel::setItems(core, a, *defaultIcon, *sl);
}

//  bool qdesigner_internal::ActionModel::dropMimeData(const QMimeData *data,
//      Qt::DropAction action, int row, int column, const QModelIndex
//      &parent)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN18qdesigner_internal11ActionModel12dropMimeDataEPK9QMimeDataN2Qt10DropActionEiiRK11QModelIndex(
    qdesigner_internal::ActionModel *self,
    const QMimeData *data,
    Qt::DropAction action,
    int row,
    int column,
    const QModelIndex *parent) {
  return self->qdesigner_internal::ActionModel::dropMimeData(
      data,
      action,
      row,
      column,
      *parent);
}
