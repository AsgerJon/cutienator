//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qabstractfileiconprovider.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qabstractfileiconprovider.h>
#include <QtGui/qicon.h>
#include <QtCore/qfileinfo.h>
#include <QtCore/qstring.h>

//  QAbstractFileIconProvider::QAbstractFileIconProvider()
extern "C" Q_DECL_EXPORT
QAbstractFileIconProvider *ritual_ZN25QAbstractFileIconProviderC1Ev() {
  return new QAbstractFileIconProvider();
}

//  QAbstractFileIconProvider::~QAbstractFileIconProvider()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QAbstractFileIconProviderD1Ev(
    QAbstractFileIconProvider *self) {
  delete self;
}

//  QIcon QAbstractFileIconProvider::icon(IconType a0) const
extern "C" Q_DECL_EXPORT
QIcon *ritual_ZNK25QAbstractFileIconProvider4iconENS_8IconTypeE(
    const QAbstractFileIconProvider *self,
    QAbstractFileIconProvider::IconType a0) {
  return new QIcon(self->icon(a0));
}

//  QIcon QAbstractFileIconProvider::icon(const QFileInfo &a0) const
extern "C" Q_DECL_EXPORT
QIcon *ritual_ZNK25QAbstractFileIconProvider4iconERK9QFileInfo(
    const QAbstractFileIconProvider *self,
    const QFileInfo *a0) {
  return new QIcon(self->icon(*a0));
}

//  QString QAbstractFileIconProvider::type(const QFileInfo &a0) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK25QAbstractFileIconProvider4typeERK9QFileInfo(
    const QAbstractFileIconProvider *self,
    const QFileInfo *a0) {
  return new QString(self->type(*a0));
}

//  void QAbstractFileIconProvider::setOptions(Options a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QAbstractFileIconProvider10setOptionsE6QFlagsINS_6OptionEE(
    QAbstractFileIconProvider *self,
    int a0) {
  self->setOptions(QFlags<QAbstractFileIconProvider::Option>::fromInt(a0));
}

//  Options QAbstractFileIconProvider::options() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK25QAbstractFileIconProvider7optionsEv(
    const QAbstractFileIconProvider *self) {
  return static_cast<int>(self->options().toInt());
}
