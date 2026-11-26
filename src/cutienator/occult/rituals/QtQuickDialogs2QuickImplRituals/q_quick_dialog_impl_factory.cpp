//  Written by dev_tooling.RitualGenerator from the records of QtQuickDialogs
//  2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qquickdialogimplfactor
//  y_p.h, Qt 6.12.0. Changes made here are lost.
#include <QtQuickDialogs2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qtquickdialogs2quickimplglobal_p.h>
#include <QtQuickDialogs2QuickImpl/QtQuickDialogs2QuickImpl>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickDialogs2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qquickdialogimplfactory_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <memory>

//  std::unique_ptr<QPlatformDialogHelper>
//      QQuickDialogImplFactory::createPlatformDialogHelper(QQuickDialogType
//      type, QObject *parent)
extern "C" Q_DECL_EXPORT
std::unique_ptr<QPlatformDialogHelper> *ritual_ZN23QQuickDialogImplFactory26createPlatformDialogHelperE16QQuickDialogTypeP7QObject(
    QQuickDialogType type,
    QObject *parent) {
  return new std::unique_ptr<QPlatformDialogHelper>(
      QQuickDialogImplFactory::createPlatformDialogHelper(
          type,
          parent));
}

//  QQuickDialogImplFactory::~QQuickDialogImplFactory()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickDialogImplFactoryD1Ev(QQuickDialogImplFactory *self) {
  delete self;
}

//  a std::unique_ptr<QPlatformDialogHelper> a ritual of
//      QQuickDialogImplFactory gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQuickDialogImplFactory__std_unique_ptr_QPlatformDialogHelper(
    std::unique_ptr<QPlatformDialogHelper> *self) {
  delete self;
}
