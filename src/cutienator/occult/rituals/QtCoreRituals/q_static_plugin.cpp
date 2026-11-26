//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qplugin.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qplugin.h>
#include <QtCore/qjsonobject.h>
#include <QtCore/qlist.h>

//  QStaticPlugin::QStaticPlugin(QtPluginInstanceFunction i,
//      QtPluginMetaDataFunction m)
extern "C" Q_DECL_EXPORT
QStaticPlugin *ritual_ZN13QStaticPluginC1EPFP7QObjectvEPF15QPluginMetaDatavE(
    void *i,
    void *m) {
  return new QStaticPlugin(
      reinterpret_cast<QtPluginInstanceFunction>(i),
      reinterpret_cast<QtPluginMetaDataFunction>(m));
}

//  QJsonObject QStaticPlugin::metaData() const
extern "C" Q_DECL_EXPORT
QJsonObject *ritual_ZNK13QStaticPlugin8metaDataEv(
    const QStaticPlugin *self) {
  return new QJsonObject(self->metaData());
}

//  QStaticPlugin::~QStaticPlugin()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QStaticPluginD1Ev(QStaticPlugin *self) {
  delete self;
}

//  QList<QStaticPlugin>::QList()
extern "C" Q_DECL_EXPORT
QList<QStaticPlugin> *ritual_list_make_QStaticPlugin() {
  return new QList<QStaticPlugin>();
}

//  void QList<QStaticPlugin>::append(const QStaticPlugin &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QStaticPlugin(
    QList<QStaticPlugin> *self,
    const QStaticPlugin *element) {
  self->append(*element);
}

//  qsizetype QList<QStaticPlugin>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QStaticPlugin(const QList<QStaticPlugin> *self) {
  return self->size();
}

//  const QStaticPlugin &QList<QStaticPlugin>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QStaticPlugin *ritual_list_at_QStaticPlugin(
    const QList<QStaticPlugin> *self,
    long long index) {
  return new QStaticPlugin(self->at(index));
}

//  QList<QStaticPlugin>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QStaticPlugin(QList<QStaticPlugin> *self) {
  delete self;
}
