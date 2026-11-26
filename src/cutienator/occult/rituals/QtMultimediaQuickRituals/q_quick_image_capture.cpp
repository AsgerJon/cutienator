//  Written by dev_tooling.RitualGenerator from the records of QtMultimediaQu
//  ick/6.12.0/QtMultimediaQuick/private/qquickimagecapture_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-26: moc's output for 'QQuickImageCapture' is
//  pasted in, cut from what the moc of Qt 6.12.0 writes for its header: Qt's
//  library keeps it to itself; added are 2 rituals that lean on what moc
//  writes for a class of the part Qt keeps to itself, whose ritual file
//  carries moc's output, drafted by a copy of the generator that lets those
//  names through. A copy of a meta-object is a second one: 'qobject_cast'
//  between it and Qt's own does not match. Kept as it is when the generator
//  runs again.
#include <QtMultimediaQuick/6.12.0/QtMultimediaQuick/private/qtmultimediaquickglobal_p.h>
#include <QtMultimediaQuick/QtMultimediaQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimediaQuick/6.12.0/QtMultimediaQuick/private/qquickimagecapture_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qimage.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qtmochelpers.h>
#include <memory>
#include <QtCore/qxptype_traits.h>
#include <QtMultimediaQuick/private/qquickimagecapture_p.h>
#include <QtCore/qurl.h>
#include <QtMultimediaQuick/private/qquickimagepreviewprovider_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from QtMultimediaQuick__QQuickImageCapture.cpp, line 1, as moc:QQuickImageCapture
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN18QQuickImageCaptureE_t {};
} // unnamed namespace

template <> constexpr inline auto QQuickImageCapture::qt_create_metaobjectdata<qt_meta_tag_ZN18QQuickImageCaptureE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "QQuickImageCapture",
        "QML.Element",
        "ImageCapture",
        "previewChanged",
        "",
        "saveToFile",
        "QUrl",
        "location",
        "_q_imageCaptured",
        "QImage",
        "preview"
    };

    QtMocHelpers::UintData qt_methods {
        // Signal 'previewChanged'
        QtMocHelpers::SignalData<void()>(3, 4, QMC::AccessPublic, QMetaType::Void),
        // Slot 'saveToFile'
        QtMocHelpers::SlotData<void(const QUrl &) const>(5, 4, QMC::AccessPublic, QMetaType::Void, {{
            { 0x80000000 | 6, 7 },
        }}),
        // Slot '_q_imageCaptured'
        QtMocHelpers::SlotData<void(int, const QImage &)>(8, 4, QMC::AccessPrivate, QMetaType::Void, {{
            { QMetaType::Int, 4 }, { 0x80000000 | 9, 4 },
        }}),
    };
    QtMocHelpers::UintData qt_properties {
        // property 'preview'
        QtMocHelpers::PropertyData<QString>(10, QMetaType::QString, QMC::DefaultPropertyFlags, 0),
    };
    QtMocHelpers::UintData qt_enums {
    };
    QtMocHelpers::UintData qt_constructors {};
    QtMocHelpers::ClassInfos qt_classinfo({
            {    1,    2 },
    });
    return QtMocHelpers::metaObjectData<QQuickImageCapture, void>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums, qt_constructors, qt_classinfo);
}
Q_CONSTINIT const QMetaObject QQuickImageCapture::staticMetaObject = { {
    QMetaObject::SuperData::link<QImageCapture::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN18QQuickImageCaptureE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN18QQuickImageCaptureE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN18QQuickImageCaptureE_t>.metaTypes,
    nullptr
} };

void QQuickImageCapture::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<QQuickImageCapture *>(_o);
    if (_c == QMetaObject::InvokeMetaMethod) {
        switch (_id) {
        case 0: _t->previewChanged(); break;
        case 1: _t->saveToFile((*reinterpret_cast<std::add_pointer_t<QUrl>>(_a[1]))); break;
        case 2: _t->_q_imageCaptured((*reinterpret_cast<std::add_pointer_t<int>>(_a[1])),(*reinterpret_cast<std::add_pointer_t<QImage>>(_a[2]))); break;
        default: ;
        }
    }
    if (_c == QMetaObject::IndexOfMethod) {
        if (QtMocHelpers::indexOfMethod<void (QQuickImageCapture::*)()>(_a, &QQuickImageCapture::previewChanged, 0))
            return;
    }
    if (_c == QMetaObject::ReadProperty) {
        void *_v = _a[0];
        switch (_id) {
        case 0: *reinterpret_cast<QString*>(_v) = _t->preview(); break;
        default: break;
        }
    }
}

const QMetaObject *QQuickImageCapture::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QQuickImageCapture::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN18QQuickImageCaptureE_t>.strings))
        return static_cast<void*>(this);
    return QImageCapture::qt_metacast(_clname);
}

int QQuickImageCapture::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QImageCapture::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 3)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 3;
    }
    if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 3)
            *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType();
        _id -= 3;
    }
    if (_c == QMetaObject::ReadProperty || _c == QMetaObject::WriteProperty
            || _c == QMetaObject::ResetProperty || _c == QMetaObject::BindableProperty
            || _c == QMetaObject::RegisterPropertyMetaType) {
        qt_static_metacall(this, _c, _id, _a);
        _id -= 1;
    }
    return _id;
}

// SIGNAL 0
void QQuickImageCapture::previewChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 0, nullptr);
}
QT_WARNING_POP

//  from ../qtmultimedia/src/multimediaquick/qquickimagecapture.cpp, line 146, as _ZN18QQuickImageCapture16_q_imageCapturedEiRK6QImage
inline void QQuickImageCapture::_q_imageCaptured(int id, const QImage &preview)
{
    QString previewId =
            QStringLiteral("preview_%1_%2").arg(m_instanceId.toString(QUuid::Id128)).arg(id);
    QQuickImagePreviewProvider::registerPreview(m_instanceId, previewId, preview);
    m_capturedImagePath = QStringLiteral("image://QtMultimediaCameraPreviewImageProvider/%2").arg(previewId);
    m_lastImage = preview;
    emit previewChanged();
}

//  from ../qtmultimedia/src/multimediaquick/qquickimagecapture.cpp, line 63, as _ZN18QQuickImageCaptureD0Ev
inline QQuickImageCapture::~QQuickImageCapture()
{
    QQuickImagePreviewProvider::cleanupInstance(m_instanceId);
}

//  from ../qtmultimedia/src/multimediaquick/qquickimagecapture.cpp, line 141, as _ZNK18QQuickImageCapture10saveToFileERK4QUrl
inline void QQuickImageCapture::saveToFile(const QUrl &location) const
{
    m_lastImage.save(location.toLocalFile());
}

//  from ../qtmultimedia/src/multimediaquick/qquickimagecapture.cpp, line 57, as _ZN18QQuickImageCaptureC1EP7QObject
inline QQuickImageCapture::QQuickImageCapture(QObject *parent)
    : QImageCapture(parent)
{
    connect(this, &QImageCapture::imageCaptured, this, &QQuickImageCapture::_q_imageCaptured);
}

//  from ../qtmultimedia/src/multimediaquick/qquickimagecapture.cpp, line 129, as _ZNK18QQuickImageCapture7previewEv
inline QString QQuickImageCapture::preview() const
{
    return m_capturedImagePath;
}
//  -----------------------------------------------------------------------

//  A QQuickImageCapture that Python can take functions over in. Every QQuickImageCapture
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickImageCaptureCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickImageCaptureCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickImageCaptureCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickImageCaptureCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickImageCaptureCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickImageCaptureCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickImageCaptureCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickImageCapture : public QQuickImageCapture {
public:
  using QQuickImageCapture::QQuickImageCapture;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickImageCaptureCall0 call = reinterpret_cast<CuteQQuickImageCaptureCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickImageCaptureCall1 call = reinterpret_cast<CuteQQuickImageCaptureCall1>(taken[1]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickImageCaptureCall2 call = reinterpret_cast<CuteQQuickImageCaptureCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickImageCaptureCall3 call = reinterpret_cast<CuteQQuickImageCaptureCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickImageCaptureCall4 call = reinterpret_cast<CuteQQuickImageCaptureCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickImageCaptureCall5 call = reinterpret_cast<CuteQQuickImageCaptureCall5>(taken[5]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickImageCaptureCall6 call = reinterpret_cast<CuteQQuickImageCaptureCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickImageCapture::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QQuickImageCapture10metaObjectEv(
    const QQuickImageCapture *self) {
  return self->metaObject();
}

//  void *QQuickImageCapture::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN18QQuickImageCapture11qt_metacastEPKc(
    QQuickImageCapture *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickImageCapture::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN18QQuickImageCapture11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickImageCapture *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickImageCapture::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18QQuickImageCapture2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickImageCapture::tr(s, c, n));
}

//  QQuickImageCapture::QQuickImageCapture(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickImageCapture *ritual_ZN18QQuickImageCaptureC1EP7QObject(
    QObject *parent) {
  return new CuteQQuickImageCapture(parent);
}

//  QQuickImageCapture::~QQuickImageCapture()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickImageCaptureD1Ev(QQuickImageCapture *self) {
  delete self;
}

//  QString QQuickImageCapture::preview() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18QQuickImageCapture7previewEv(
    const QQuickImageCapture *self) {
  return new QString(self->preview());
}

//  void QQuickImageCapture::previewChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickImageCapture14previewChangedEv(
    QQuickImageCapture *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickImageCapture")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "previewChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "previewChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickImageCapture::_q_imageCaptured(int a0, const QImage &a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickImageCapture16_q_imageCapturedEiRK6QImage(
    QQuickImageCapture *self,
    int a0,
    const QImage *a1) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickImageCapture")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "_q_imageCaptured(int,const QImage &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "_q_imageCaptured(int,const QImage &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&a0)),
      const_cast<void *>(static_cast<const void *>(a1)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  a Python function taken by a CuteQQuickImageCapture, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickImageCapture(
    QQuickImageCapture *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickImageCapture *>(self)->take(key, call);
}
