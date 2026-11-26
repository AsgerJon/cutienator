//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/actionrepository_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/actionrepository_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qabstractitemmodel.h>
#include <QtGui/qaction.h>
#include <QtCore/qitemselectionmodel.h>
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/private/actionrepository_p.h>
#include <QtDesigner/private/qtresourceview_p.h>
#include <QtDesigner/private/iconloader_p.h>
#include <QtDesigner/private/qdesigner_utils_p.h>
#include <QtDesigner/abstractformeditor.h>
#include <QtDesigner/propertysheet.h>
#include <QtDesigner/qextensionmanager.h>
#include <QtWidgets/qtoolbutton.h>
#include <QtWidgets/qheaderview.h>
#include <QtWidgets/qtoolbar.h>
#include <QtWidgets/qmenu.h>
#include <QtGui/qpixmap.h>
#include <QtGui/qaction.h>
#include <QtGui/qdrag.h>
#include <QtGui/qevent.h>
#include <QtGui/qstandarditemmodel.h>
#include <QtCore/qset.h>
#include <QtCore/qdebug.h>
#include <QtCore/qmetaobject.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from ../qttools/src/designer/src/lib/shared/actionrepository.cpp, line 40, as local:actionrepository.cpp:actionOfItem
static inline QAction *actionOfItem(const QStandardItem* item)
{
    return qvariant_cast<QAction*>(item->data(qdesigner_internal::ActionModel::ActionRole));
}

//  from ../qttools/src/designer/src/lib/shared/actionrepository.cpp, line 421, as _ZNK18qdesigner_internal14ActionListView13currentActionEv
namespace qdesigner_internal {
using namespace Qt::StringLiterals;
inline QAction *ActionListView::currentAction() const
{
    return m_model->actionAt(currentIndex());
}
}  // namespace qdesigner_internal

//  from ../qttools/src/designer/src/lib/shared/actionrepository.cpp, line 514, as _ZNK18qdesigner_internal10ActionView8viewModeEv
namespace qdesigner_internal {
using namespace Qt::StringLiterals;
inline int ActionView::viewMode() const
{
    return currentWidget() == m_actionListView ? IconView : DetailedView;
}
}  // namespace qdesigner_internal

//  from ../qttools/src/designer/src/lib/shared/actionrepository.cpp, line 519, as _ZN18qdesigner_internal10ActionView11setViewModeEi
namespace qdesigner_internal {
using namespace Qt::StringLiterals;
inline void ActionView::setViewMode(int lm)
{
    if (viewMode() == lm)
        return;

    switch (lm) {
    case IconView:
        setCurrentWidget(m_actionListView);
        break;
    case DetailedView:
        setCurrentWidget(m_actionTreeView);
        break;
    default:
        break;
    }
}
}  // namespace qdesigner_internal

//  from ../qttools/src/designer/src/lib/shared/actionrepository.cpp, line 576, as _ZN18qdesigner_internal10ActionView16setSelectionModeEN17QAbstractItemView13SelectionModeE
namespace qdesigner_internal {
using namespace Qt::StringLiterals;
inline void ActionView::setSelectionMode(QAbstractItemView::SelectionMode sm)
{
    m_actionTreeView->setSelectionMode(sm);
    m_actionListView->setSelectionMode(sm);
}
}  // namespace qdesigner_internal

//  from ../qttools/src/designer/src/lib/shared/actionrepository.cpp, line 582, as _ZNK18qdesigner_internal10ActionView13selectionModeEv
namespace qdesigner_internal {
using namespace Qt::StringLiterals;
inline QAbstractItemView::SelectionMode ActionView::selectionMode() const
{
    return m_actionListView->selectionMode();
}
}  // namespace qdesigner_internal

//  from ../qttools/src/designer/src/lib/shared/actionrepository.cpp, line 571, as _ZNK18qdesigner_internal10ActionView13currentActionEv
namespace qdesigner_internal {
using namespace Qt::StringLiterals;
inline QAction *ActionView::currentAction() const
{
    return m_actionListView->currentAction();
}
}  // namespace qdesigner_internal

//  from ../qttools/src/designer/src/lib/shared/actionrepository.cpp, line 566, as _ZN18qdesigner_internal10ActionView15setCurrentIndexERK11QModelIndex
namespace qdesigner_internal {
using namespace Qt::StringLiterals;
inline void ActionView::setCurrentIndex(const QModelIndex &index)
{
    m_actionTreeView->setCurrentIndex(index);
}
}  // namespace qdesigner_internal

//  from ../qttools/src/designer/src/lib/shared/actionrepository.cpp, line 592, as _ZNK18qdesigner_internal10ActionView15selectedActionsEv
namespace qdesigner_internal {
using namespace Qt::StringLiterals;
inline ActionView::ActionList ActionView::selectedActions() const
{
    ActionList rc;
    const QModelIndexList &indexes = selection().indexes();
    for (const QModelIndex &index : indexes) {
        if (index.column() == 0)
            rc += actionOfItem(m_model->itemFromIndex(index));
    }
    return rc;
}
}  // namespace qdesigner_internal

//  from ../qttools/src/designer/src/lib/shared/actionrepository.cpp, line 587, as _ZNK18qdesigner_internal10ActionView9selectionEv
namespace qdesigner_internal {
using namespace Qt::StringLiterals;
inline QItemSelection ActionView::selection() const
{
    return  m_actionListView->selectionModel()->selection();
}
}  // namespace qdesigner_internal
//  -----------------------------------------------------------------------

//  const QMetaObject *qdesigner_internal::ActionView::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18qdesigner_internal10ActionView10metaObjectEv(
    const qdesigner_internal::ActionView *self) {
  return self->metaObject();
}

//  void *qdesigner_internal::ActionView::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN18qdesigner_internal10ActionView11qt_metacastEPKc(
    qdesigner_internal::ActionView *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int qdesigner_internal::ActionView::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN18qdesigner_internal10ActionView11qt_metacallEN11QMetaObject4CallEiPPv(
    qdesigner_internal::ActionView *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  void
//      qdesigner_internal::ActionView::initialize(QDesignerFormEditorInterfa
//      ce *core)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal10ActionView10initializeEP28QDesignerFormEditorInterface(
    qdesigner_internal::ActionView *self,
    QDesignerFormEditorInterface *core) {
  self->initialize(core);
}

//  int qdesigner_internal::ActionView::viewMode() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18qdesigner_internal10ActionView8viewModeEv(
    const qdesigner_internal::ActionView *self) {
  return self->viewMode();
}

//  void qdesigner_internal::ActionView::setViewMode(int lm)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal10ActionView11setViewModeEi(
    qdesigner_internal::ActionView *self,
    int lm) {
  self->setViewMode(lm);
}

//  void qdesigner_internal::ActionView::setSelectionMode(QAbstractItemView::
//      SelectionMode sm)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal10ActionView16setSelectionModeEN17QAbstractItemView13SelectionModeE(
    qdesigner_internal::ActionView *self,
    QAbstractItemView::SelectionMode sm) {
  self->setSelectionMode(sm);
}

//  QAbstractItemView::SelectionMode
//      qdesigner_internal::ActionView::selectionMode() const
extern "C" Q_DECL_EXPORT
QAbstractItemView::SelectionMode ritual_ZNK18qdesigner_internal10ActionView13selectionModeEv(
    const qdesigner_internal::ActionView *self) {
  return self->selectionMode();
}

//  ActionModel *qdesigner_internal::ActionView::model() const
extern "C" Q_DECL_EXPORT
qdesigner_internal::ActionModel *ritual_ZNK18qdesigner_internal10ActionView5modelEv(
    const qdesigner_internal::ActionView *self) {
  return self->model();
}

//  QAction *qdesigner_internal::ActionView::currentAction() const
extern "C" Q_DECL_EXPORT
QAction *ritual_ZNK18qdesigner_internal10ActionView13currentActionEv(
    const qdesigner_internal::ActionView *self) {
  return self->currentAction();
}

//  void qdesigner_internal::ActionView::setCurrentIndex(const QModelIndex
//      &index)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal10ActionView15setCurrentIndexERK11QModelIndex(
    qdesigner_internal::ActionView *self,
    const QModelIndex *index) {
  self->setCurrentIndex(*index);
}

//  ActionList qdesigner_internal::ActionView::selectedActions() const
extern "C" Q_DECL_EXPORT
QList<QAction *> *ritual_ZNK18qdesigner_internal10ActionView15selectedActionsEv(
    const qdesigner_internal::ActionView *self) {
  return new QList<QAction *>(self->selectedActions());
}

//  QItemSelection qdesigner_internal::ActionView::selection() const
extern "C" Q_DECL_EXPORT
QItemSelection *ritual_ZNK18qdesigner_internal10ActionView9selectionEv(
    const qdesigner_internal::ActionView *self) {
  return new QItemSelection(self->selection());
}

//  void qdesigner_internal::ActionView::filter(const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal10ActionView6filterERK7QString(
    qdesigner_internal::ActionView *self,
    const QString *text) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "qdesigner_internal::ActionView")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "filter(const QString &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "filter(const QString &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(text)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void qdesigner_internal::ActionView::selectAll()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal10ActionView9selectAllEv(
    qdesigner_internal::ActionView *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "qdesigner_internal::ActionView")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "selectAll()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "selectAll()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void qdesigner_internal::ActionView::clearSelection()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal10ActionView14clearSelectionEv(
    qdesigner_internal::ActionView *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "qdesigner_internal::ActionView")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "clearSelection()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "clearSelection()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void qdesigner_internal::ActionView::selectAction(QAction *a)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal10ActionView12selectActionEP7QAction(
    qdesigner_internal::ActionView *self,
    QAction *a) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "qdesigner_internal::ActionView")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "selectAction(QAction *)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "selectAction(QAction *)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&a)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void
//      qdesigner_internal::ActionView::contextMenuRequested(QContextMenuEven
//      t *event, QAction *a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal10ActionView20contextMenuRequestedEP17QContextMenuEventP7QAction(
    qdesigner_internal::ActionView *self,
    QContextMenuEvent *event,
    QAction *a1) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "qdesigner_internal::ActionView")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "contextMenuRequested(QContextMenuEvent *,QAction *)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "contextMenuRequested(QContextMenuEvent *,QAction *)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&event)),
      const_cast<void *>(static_cast<const void *>(&a1)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void qdesigner_internal::ActionView::currentActionChanged(QAction
//      *action)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal10ActionView20currentActionChangedEP7QAction(
    qdesigner_internal::ActionView *self,
    QAction *action) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "qdesigner_internal::ActionView")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "currentActionChanged(QAction *)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "currentActionChanged(QAction *)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&action)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void qdesigner_internal::ActionView::activated(QAction *action, int
//      column)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal10ActionView9activatedEP7QActioni(
    qdesigner_internal::ActionView *self,
    QAction *action,
    int column) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "qdesigner_internal::ActionView")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "activated(QAction *,int)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "activated(QAction *,int)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&action)),
      const_cast<void *>(static_cast<const void *>(&column)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void qdesigner_internal::ActionView::selectionChanged(const
//      QItemSelection &selected, const QItemSelection &deselected)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal10ActionView16selectionChangedERK14QItemSelectionS3_(
    qdesigner_internal::ActionView *self,
    const QItemSelection *selected,
    const QItemSelection *deselected) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "qdesigner_internal::ActionView")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "selectionChanged(const QItemSelection &,const QItemSelection &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "selectionChanged(const QItemSelection &,const QItemSelection &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(selected)),
      const_cast<void *>(static_cast<const void *>(deselected)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void qdesigner_internal::ActionView::resourceImageDropped(const QString
//      &data, QAction *action)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal10ActionView20resourceImageDroppedERK7QStringP7QAction(
    qdesigner_internal::ActionView *self,
    const QString *data,
    QAction *action) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "qdesigner_internal::ActionView")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "resourceImageDropped(const QString &,QAction *)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "resourceImageDropped(const QString &,QAction *)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(data)),
      const_cast<void *>(static_cast<const void *>(&action)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void qdesigner_internal::ActionView::slotCurrentChanged(QAction *action)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal10ActionView18slotCurrentChangedEP7QAction(
    qdesigner_internal::ActionView *self,
    QAction *action) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "qdesigner_internal::ActionView")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "slotCurrentChanged(QAction *)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "slotCurrentChanged(QAction *)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&action)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}
