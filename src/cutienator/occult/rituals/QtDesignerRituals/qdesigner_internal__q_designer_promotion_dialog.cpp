//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/qdesigner_promotiondialog_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/qdesigner_promotiondialog_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qitemselectionmodel.h>
#include <QtCore/qpoint.h>
#include <QtCore/qlist.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/private/qdesigner_promotiondialog_p.h>
#include <QtDesigner/private/promotionmodel_p.h>
#include <QtDesigner/private/iconloader_p.h>
#include <QtDesigner/private/widgetdatabase_p.h>
#include <QtDesigner/private/signalslotdialog_p.h>
#include <QtDesigner/abstractformeditor.h>
#include <QtDesigner/abstractformwindow.h>
#include <QtDesigner/abstractpromotioninterface.h>
#include <QtDesigner/abstractwidgetdatabase.h>
#include <QtDesigner/abstractintegration.h>
#include <QtDesigner/private/abstractdialoggui_p.h>
#include <QtWidgets/qboxlayout.h>
#include <QtWidgets/qformlayout.h>
#include <QtWidgets/qdialogbuttonbox.h>
#include <QtWidgets/qtreeview.h>
#include <QtWidgets/qheaderview.h>
#include <QtWidgets/qpushbutton.h>
#include <QtWidgets/qcombobox.h>
#include <QtWidgets/qlineedit.h>
#include <QtWidgets/qcheckbox.h>
#include <QtWidgets/qlabel.h>
#include <QtWidgets/qlayoutitem.h>
#include <QtWidgets/qmenu.h>
#include <QtGui/qaction.h>
#include <QtGui/qvalidator.h>
#include <QtCore/qitemselectionmodel.h>
#include <QtCore/qtimer.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from ../qttools/src/designer/src/lib/shared/qdesigner_promotiondialog.cpp, line 279, as _ZN18qdesigner_internal24QDesignerPromotionDialog14baseClassNamesEPK27QDesignerPromotionInterface
namespace qdesigner_internal {
using namespace Qt::StringLiterals;
inline const QStringList &QDesignerPromotionDialog::baseClassNames(const QDesignerPromotionInterface *promotion) {
        using WidgetDataBaseItemList = QList<QDesignerWidgetDataBaseItemInterface *>;
        static QStringList rc;
        if (rc.isEmpty()) {
            // Convert the item list into a string list.
            const WidgetDataBaseItemList dbItems =  promotion->promotionBaseClasses();
            for (auto *item : dbItems)
                rc.append(item->name());
        }
        return rc;
    }
}  // namespace qdesigner_internal
//  -----------------------------------------------------------------------

//  const QMetaObject
//      *qdesigner_internal::QDesignerPromotionDialog::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18qdesigner_internal24QDesignerPromotionDialog10metaObjectEv(
    const qdesigner_internal::QDesignerPromotionDialog *self) {
  return self->metaObject();
}

//  void *qdesigner_internal::QDesignerPromotionDialog::qt_metacast(const
//      char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN18qdesigner_internal24QDesignerPromotionDialog11qt_metacastEPKc(
    qdesigner_internal::QDesignerPromotionDialog *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int qdesigner_internal::QDesignerPromotionDialog::qt_metacall(QMetaObject
//      ::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN18qdesigner_internal24QDesignerPromotionDialog11qt_metacallEN11QMetaObject4CallEiPPv(
    qdesigner_internal::QDesignerPromotionDialog *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  const QStringList
//      &qdesigner_internal::QDesignerPromotionDialog::baseClassNames(const
//      QDesignerPromotionInterface *promotion)
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZN18qdesigner_internal24QDesignerPromotionDialog14baseClassNamesEPK27QDesignerPromotionInterface(
    const QDesignerPromotionInterface *promotion) {
  return new QList<QString>(
      qdesigner_internal::QDesignerPromotionDialog::baseClassNames(
          promotion));
}

//  void qdesigner_internal::QDesignerPromotionDialog::selectedBaseClassChang
//      ed(const QString &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal24QDesignerPromotionDialog24selectedBaseClassChangedERK7QString(
    qdesigner_internal::QDesignerPromotionDialog *self,
    const QString *a0) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "qdesigner_internal::QDesignerPromotionDialog")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "selectedBaseClassChanged(const QString &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "selectedBaseClassChanged(const QString &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(a0)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void qdesigner_internal::QDesignerPromotionDialog::slotRemove()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal24QDesignerPromotionDialog10slotRemoveEv(
    qdesigner_internal::QDesignerPromotionDialog *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "qdesigner_internal::QDesignerPromotionDialog")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "slotRemove()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "slotRemove()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void qdesigner_internal::QDesignerPromotionDialog::slotAcceptPromoteTo()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal24QDesignerPromotionDialog19slotAcceptPromoteToEv(
    qdesigner_internal::QDesignerPromotionDialog *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "qdesigner_internal::QDesignerPromotionDialog")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "slotAcceptPromoteTo()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "slotAcceptPromoteTo()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void
//      qdesigner_internal::QDesignerPromotionDialog::slotSelectionChanged(co
//      nst QItemSelection &a0, const QItemSelection &a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal24QDesignerPromotionDialog20slotSelectionChangedERK14QItemSelectionS3_(
    qdesigner_internal::QDesignerPromotionDialog *self,
    const QItemSelection *a0,
    const QItemSelection *a1) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "qdesigner_internal::QDesignerPromotionDialog")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "slotSelectionChanged(const QItemSelection &,const QItemSelection &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "slotSelectionChanged(const QItemSelection &,const QItemSelection &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(a0)),
      const_cast<void *>(static_cast<const void *>(a1)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void qdesigner_internal::QDesignerPromotionDialog::slotIncludeFileChanged
//      (QDesignerWidgetDataBaseItemInterface *a0, const QString
//      &includeFile)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal24QDesignerPromotionDialog22slotIncludeFileChangedEP36QDesignerWidgetDataBaseItemInterfaceRK7QString(
    qdesigner_internal::QDesignerPromotionDialog *self,
    QDesignerWidgetDataBaseItemInterface *a0,
    const QString *includeFile) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "qdesigner_internal::QDesignerPromotionDialog")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "slotIncludeFileChanged(QDesignerWidgetDataBaseItemInterface *,const QString &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "slotIncludeFileChanged(QDesignerWidgetDataBaseItemInterface *,const QString &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&a0)),
      const_cast<void *>(static_cast<const void *>(includeFile)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void qdesigner_internal::QDesignerPromotionDialog::slotClassNameChanged(Q
//      DesignerWidgetDataBaseItemInterface *a0, const QString &newName)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal24QDesignerPromotionDialog20slotClassNameChangedEP36QDesignerWidgetDataBaseItemInterfaceRK7QString(
    qdesigner_internal::QDesignerPromotionDialog *self,
    QDesignerWidgetDataBaseItemInterface *a0,
    const QString *newName) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "qdesigner_internal::QDesignerPromotionDialog")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "slotClassNameChanged(QDesignerWidgetDataBaseItemInterface *,const QString &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "slotClassNameChanged(QDesignerWidgetDataBaseItemInterface *,const QString &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&a0)),
      const_cast<void *>(static_cast<const void *>(newName)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void qdesigner_internal::QDesignerPromotionDialog::slotUpdateFromWidgetDa
//      tabase()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal24QDesignerPromotionDialog28slotUpdateFromWidgetDatabaseEv(
    qdesigner_internal::QDesignerPromotionDialog *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "qdesigner_internal::QDesignerPromotionDialog")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "slotUpdateFromWidgetDatabase()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "slotUpdateFromWidgetDatabase()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void qdesigner_internal::QDesignerPromotionDialog::slotTreeViewContextMen
//      u(const QPoint &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal24QDesignerPromotionDialog23slotTreeViewContextMenuERK6QPoint(
    qdesigner_internal::QDesignerPromotionDialog *self,
    const QPoint *a0) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "qdesigner_internal::QDesignerPromotionDialog")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "slotTreeViewContextMenu(const QPoint &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "slotTreeViewContextMenu(const QPoint &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(a0)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void qdesigner_internal::QDesignerPromotionDialog::slotEditSignalsSlots()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal24QDesignerPromotionDialog20slotEditSignalsSlotsEv(
    qdesigner_internal::QDesignerPromotionDialog *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "qdesigner_internal::QDesignerPromotionDialog")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "slotEditSignalsSlots()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "slotEditSignalsSlots()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}
