//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qfileiconprovider.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qfileiconprovider.h>
#include <QtGui/qicon.h>
#include <QtCore/qfileinfo.h>

//  QFileIconProvider::QFileIconProvider()
extern "C" Q_DECL_EXPORT
QFileIconProvider *ritual_ZN17QFileIconProviderC1Ev() {
  return new QFileIconProvider();
}

//  QFileIconProvider::~QFileIconProvider()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QFileIconProviderD1Ev(QFileIconProvider *self) {
  delete self;
}

//  QIcon QFileIconProvider::icon(IconType type) const
extern "C" Q_DECL_EXPORT
QIcon *ritual_ZNK17QFileIconProvider4iconEN25QAbstractFileIconProvider8IconTypeE(
    const QFileIconProvider *self,
    QAbstractFileIconProvider::IconType type) {
  return new QIcon(self->icon(type));
}

//  QIcon QFileIconProvider::icon(const QFileInfo &info) const
extern "C" Q_DECL_EXPORT
QIcon *ritual_ZNK17QFileIconProvider4iconERK9QFileInfo(
    const QFileIconProvider *self,
    const QFileInfo *info) {
  return new QIcon(self->icon(*info));
}
