//  Written by hand on 2026-11-25 from
//  QtAxServer/6.12.0/QtAxServer/private/qaxserverbase_p.h, Qt 6.12.0,
//  from Qt's source. Kept as it is when the generator runs again.
//  Qt builds ActiveQt for Windows only. AxServer is a static library,
//  all of it compiled into ours, so the class is taken as exported.
//  What Windows has, as its handles, interfaces and structs, is passed
//  as an address, a 'REFIID' as the address of its 'IID', and the
//  function 'Draw' calls back as a 'void *'. A 'DWORD', a 'ULONG'
//  and an 'LCID' are passed as an 'unsigned long'; a 'LONG', a
//  'DISPID' and the 'HRESULT' given back as a 'long'; a 'BOOL' as
//  an 'int', a 'UINT' as an 'unsigned int', a 'WORD' as an
//  'unsigned short'; a 'WPARAM' as an 'unsigned long long', an
//  'LPARAM' and an 'LRESULT' as a 'long long'.
//  'TranslateAccelerator' and 'GetClassInfo' are named as Qt writes
//  them; where 'UNICODE' is defined a macro of Windows makes them
//  'TranslateAcceleratorW' and 'GetClassInfoW', here and in Qt alike.
//  The class has no Q_OBJECT: no 'metaObject()' and no 'tr'.
//  Not written: 'create', taking a 'RECT &'; 'SetHostNames' and the
//  'Load', 'Save' and 'SaveCompleted' of IPersistFile, taking an
//  'LPCOLESTR', a 'const wchar_t *' no row has a word for; and
//  'qt_metacall'.
#include <QtCore/qglobal.h>
#if defined(Q_OS_WIN)
#include <QtAxServer/6.12.0/QtAxServer/private/qaxserverbase_p.h>
#include <QtCore/qcoreevent.h>
#include <QtCore/qmetaobject.h>
#include <QtWidgets/qmenu.h>
#include <QtWidgets/qmenubar.h>
#include <cstring>

//  A QAxServerBase that Python can take functions over in. Every
//  QAxServerBase Python makes is one. Each function below asks the
//  Python function handed over for it, and runs Qt's own without
//  one.
typedef HRESULT (*CuteQAxServerBaseCall0)(const void *, const IID *, void **, int *);
typedef ULONG (*CuteQAxServerBaseCall1)(const void *, int *);
typedef ULONG (*CuteQAxServerBaseCall2)(const void *, int *);
typedef void * (*CuteQAxServerBaseCall3)(const void *, int *);
typedef void (*CuteQAxServerBaseCall4)(const void *, const char *, int *);
typedef bool (*CuteQAxServerBaseCall5)(const void *, const char *, int *);
typedef void * (*CuteQAxServerBaseCall6)(const void *, int *);
typedef void (*CuteQAxServerBaseCall7)(const void *, int, const QString *, const QString *, const QString *, int *);
typedef HRESULT (*CuteQAxServerBaseCall8)(const void *, UINT *, int *);
typedef HRESULT (*CuteQAxServerBaseCall9)(const void *, UINT, LCID, ITypeInfo **, int *);
typedef HRESULT (*CuteQAxServerBaseCall10)(const void *, const IID *, LPOLESTR *, UINT, LCID, DISPID *, int *);
typedef HRESULT (*CuteQAxServerBaseCall11)(const void *, DISPID, const IID *, LCID, WORD, DISPPARAMS *, VARIANT *, EXCEPINFO *, UINT *, int *);
typedef HRESULT (*CuteQAxServerBaseCall12)(const void *, IOleClientSite *, int *);
typedef HRESULT (*CuteQAxServerBaseCall13)(const void *, IOleClientSite **, int *);
typedef HRESULT (*CuteQAxServerBaseCall14)(const void *, DWORD, int *);
typedef HRESULT (*CuteQAxServerBaseCall15)(const void *, DWORD, IMoniker *, int *);
typedef HRESULT (*CuteQAxServerBaseCall16)(const void *, DWORD, DWORD, IMoniker **, int *);
typedef HRESULT (*CuteQAxServerBaseCall17)(const void *, IDataObject *, BOOL, DWORD, int *);
typedef HRESULT (*CuteQAxServerBaseCall18)(const void *, DWORD, IDataObject **, int *);
typedef HRESULT (*CuteQAxServerBaseCall19)(const void *, LONG, LPMSG, IOleClientSite *, LONG, HWND, LPCRECT, int *);
typedef HRESULT (*CuteQAxServerBaseCall20)(const void *, IEnumOLEVERB **, int *);
typedef HRESULT (*CuteQAxServerBaseCall21)(const void *, int *);
typedef HRESULT (*CuteQAxServerBaseCall22)(const void *, int *);
typedef HRESULT (*CuteQAxServerBaseCall23)(const void *, CLSID *, int *);
typedef HRESULT (*CuteQAxServerBaseCall24)(const void *, DWORD, LPOLESTR *, int *);
typedef HRESULT (*CuteQAxServerBaseCall25)(const void *, DWORD, SIZEL *, int *);
typedef HRESULT (*CuteQAxServerBaseCall26)(const void *, DWORD, SIZEL *, int *);
typedef HRESULT (*CuteQAxServerBaseCall27)(const void *, IAdviseSink *, DWORD *, int *);
typedef HRESULT (*CuteQAxServerBaseCall28)(const void *, DWORD, int *);
typedef HRESULT (*CuteQAxServerBaseCall29)(const void *, IEnumSTATDATA **, int *);
typedef HRESULT (*CuteQAxServerBaseCall30)(const void *, DWORD, DWORD *, int *);
typedef HRESULT (*CuteQAxServerBaseCall31)(const void *, LOGPALETTE *, int *);
typedef HRESULT (*CuteQAxServerBaseCall32)(const void *, CONTROLINFO *, int *);
typedef HRESULT (*CuteQAxServerBaseCall33)(const void *, MSG *, int *);
typedef HRESULT (*CuteQAxServerBaseCall34)(const void *, DISPID, int *);
typedef HRESULT (*CuteQAxServerBaseCall35)(const void *, BOOL, int *);
typedef HRESULT (*CuteQAxServerBaseCall36)(const void *, DWORD, LONG, void *, DVTARGETDEVICE *, HDC, HDC, LPCRECTL, LPCRECTL, void *, ULONG_PTR, int *);
typedef HRESULT (*CuteQAxServerBaseCall37)(const void *, DWORD, LONG, void *, DVTARGETDEVICE *, HDC, LOGPALETTE **, int *);
typedef HRESULT (*CuteQAxServerBaseCall38)(const void *, DWORD, LONG, void *, DWORD *, int *);
typedef HRESULT (*CuteQAxServerBaseCall39)(const void *, DWORD, int *);
typedef HRESULT (*CuteQAxServerBaseCall40)(const void *, DWORD, DWORD, IAdviseSink *, int *);
typedef HRESULT (*CuteQAxServerBaseCall41)(const void *, DWORD *, DWORD *, IAdviseSink **, int *);
typedef HRESULT (*CuteQAxServerBaseCall42)(const void *, DWORD, LONG, DVTARGETDEVICE *, LPSIZEL, int *);
typedef HRESULT (*CuteQAxServerBaseCall43)(const void *, HWND *, int *);
typedef HRESULT (*CuteQAxServerBaseCall44)(const void *, BOOL, int *);
typedef HRESULT (*CuteQAxServerBaseCall45)(const void *, int *);
typedef HRESULT (*CuteQAxServerBaseCall46)(const void *, int *);
typedef HRESULT (*CuteQAxServerBaseCall47)(const void *, LPCRECT, LPCRECT, int *);
typedef HRESULT (*CuteQAxServerBaseCall48)(const void *, int *);
typedef HRESULT (*CuteQAxServerBaseCall49)(const void *, LPMSG, int *);
typedef HRESULT (*CuteQAxServerBaseCall50)(const void *, BOOL, int *);
typedef HRESULT (*CuteQAxServerBaseCall51)(const void *, BOOL, int *);
typedef HRESULT (*CuteQAxServerBaseCall52)(const void *, LPCRECT, IOleInPlaceUIWindow *, BOOL, int *);
typedef HRESULT (*CuteQAxServerBaseCall53)(const void *, BOOL, int *);
typedef HRESULT (*CuteQAxServerBaseCall54)(const void *, ITypeInfo **, int *);
typedef HRESULT (*CuteQAxServerBaseCall55)(const void *, DWORD, GUID *, int *);
typedef HRESULT (*CuteQAxServerBaseCall56)(const void *, IEnumConnectionPoints **, int *);
typedef HRESULT (*CuteQAxServerBaseCall57)(const void *, const IID *, IConnectionPoint **, int *);
typedef HRESULT (*CuteQAxServerBaseCall58)(const void *, CLSID *, int *);
typedef HRESULT (*CuteQAxServerBaseCall59)(const void *, int *);
typedef HRESULT (*CuteQAxServerBaseCall60)(const void *, LPSTREAM, int *);
typedef HRESULT (*CuteQAxServerBaseCall61)(const void *, LPSTREAM, BOOL, int *);
typedef HRESULT (*CuteQAxServerBaseCall62)(const void *, ULARGE_INTEGER *, int *);
typedef HRESULT (*CuteQAxServerBaseCall63)(const void *, int *);
typedef HRESULT (*CuteQAxServerBaseCall64)(const void *, IStorage *, int *);
typedef HRESULT (*CuteQAxServerBaseCall65)(const void *, IStorage *, int *);
typedef HRESULT (*CuteQAxServerBaseCall66)(const void *, IStorage *, BOOL, int *);
typedef HRESULT (*CuteQAxServerBaseCall67)(const void *, IStorage *, int *);
typedef HRESULT (*CuteQAxServerBaseCall68)(const void *, int *);
typedef HRESULT (*CuteQAxServerBaseCall69)(const void *, IPropertyBag *, IErrorLog *, int *);
typedef HRESULT (*CuteQAxServerBaseCall70)(const void *, IPropertyBag *, BOOL, BOOL, int *);
typedef HRESULT (*CuteQAxServerBaseCall71)(const void *, LPOLESTR *, int *);
typedef HRESULT (*CuteQAxServerBaseCall72)(const void *, FORMATETC *, STGMEDIUM *, int *);
typedef HRESULT (*CuteQAxServerBaseCall73)(const void *, FORMATETC *, STGMEDIUM *, int *);
typedef HRESULT (*CuteQAxServerBaseCall74)(const void *, FORMATETC *, int *);
typedef HRESULT (*CuteQAxServerBaseCall75)(const void *, FORMATETC *, FORMATETC *, int *);
typedef HRESULT (*CuteQAxServerBaseCall76)(const void *, FORMATETC *, STGMEDIUM *, BOOL, int *);
typedef HRESULT (*CuteQAxServerBaseCall77)(const void *, DWORD, IEnumFORMATETC **, int *);
typedef HRESULT (*CuteQAxServerBaseCall78)(const void *, FORMATETC *, DWORD, IAdviseSink *, DWORD *, int *);
typedef HRESULT (*CuteQAxServerBaseCall79)(const void *, DWORD, int *);
typedef HRESULT (*CuteQAxServerBaseCall80)(const void *, IEnumSTATDATA **, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAxServerBaseCall81)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAxServerBaseCall82)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAxServerBaseCall83)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAxServerBaseCall84)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAxServerBaseCall85)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAxServerBaseCall86)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAxServerBaseCall87)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQAxServerBase : public QAxServerBase {
public:
  using QAxServerBase::QAxServerBase;
  void *taken[88] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN8IUnknown14QueryInterfaceERK5_GUIDPPv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8IUnknown6AddRefEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8IUnknown7ReleaseEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK13IAxServerBase10ClientSiteEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13IAxServerBase19EmitPropertyChangedEPKc")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13IAxServerBase25EmitRequestPropertyChangeEPKc")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK13IAxServerBase10GetQObjectEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13IAxServerBase11ReportErrorEiRK7QStringS2_S2_")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9IDispatch16GetTypeInfoCountEPj")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9IDispatch11GetTypeInfoEjmPP9ITypeInfo")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9IDispatch13GetIDsOfNamesERK5_GUIDPPwjmPl")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9IDispatch6InvokeElRK5_GUIDmtP13tagDISPPARAMSP10tagVARIANTP12tagEXCEPINFOPj")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10IOleObject13SetClientSiteEP14IOleClientSite")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10IOleObject13GetClientSiteEPP14IOleClientSite")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10IOleObject5CloseEm")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10IOleObject10SetMonikerEmP8IMoniker")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10IOleObject10GetMonikerEmmPP8IMoniker")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10IOleObject12InitFromDataEP11IDataObjectim")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10IOleObject16GetClipboardDataEmPP11IDataObject")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10IOleObject6DoVerbElP6tagMSGP14IOleClientSitelP6HWND__PK7tagRECT")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10IOleObject9EnumVerbsEPP12IEnumOLEVERB")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10IOleObject6UpdateEv")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10IOleObject10IsUpToDateEv")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10IOleObject14GetUserClassIDEP5_GUID")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10IOleObject11GetUserTypeEmPPw")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10IOleObject9SetExtentEmP7tagSIZE")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10IOleObject9GetExtentEmP7tagSIZE")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10IOleObject6AdviseEP11IAdviseSinkPm")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10IOleObject8UnadviseEm")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10IOleObject10EnumAdviseEPP13IEnumSTATDATA")) {
      taken[29] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10IOleObject13GetMiscStatusEmPm")) {
      taken[30] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10IOleObject14SetColorSchemeEP13tagLOGPALETTE")) {
      taken[31] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11IOleControl14GetControlInfoEP14tagCONTROLINFO")) {
      taken[32] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11IOleControl10OnMnemonicEP6tagMSG")) {
      taken[33] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11IOleControl23OnAmbientPropertyChangeEl")) {
      taken[34] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11IOleControl12FreezeEventsEi")) {
      taken[35] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11IViewObject4DrawEmlPvP17tagDVTARGETDEVICEP5HDC__S4_PK6_RECTLS7_PFiyEy")) {
      taken[36] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11IViewObject11GetColorSetEmlPvP17tagDVTARGETDEVICEP5HDC__PP13tagLOGPALETTE")) {
      taken[37] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11IViewObject6FreezeEmlPvPm")) {
      taken[38] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11IViewObject8UnfreezeEm")) {
      taken[39] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11IViewObject9SetAdviseEmmP11IAdviseSink")) {
      taken[40] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11IViewObject9GetAdviseEPmS0_PP11IAdviseSink")) {
      taken[41] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12IViewObject29GetExtentEmlP17tagDVTARGETDEVICEP7tagSIZE")) {
      taken[42] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10IOleWindow9GetWindowEPP6HWND__")) {
      taken[43] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10IOleWindow20ContextSensitiveHelpEi")) {
      taken[44] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17IOleInPlaceObject17InPlaceDeactivateEv")) {
      taken[45] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17IOleInPlaceObject12UIDeactivateEv")) {
      taken[46] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17IOleInPlaceObject14SetObjectRectsEPK7tagRECTS2_")) {
      taken[47] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17IOleInPlaceObject17ReactivateAndUndoEv")) {
      taken[48] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN23IOleInPlaceActiveObject20TranslateAcceleratorEP6tagMSG")) {
      taken[49] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN23IOleInPlaceActiveObject21OnFrameWindowActivateEi")) {
      taken[50] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN23IOleInPlaceActiveObject19OnDocWindowActivateEi")) {
      taken[51] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN23IOleInPlaceActiveObject12ResizeBorderEPK7tagRECTP19IOleInPlaceUIWindowi")) {
      taken[52] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN23IOleInPlaceActiveObject14EnableModelessEi")) {
      taken[53] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17IProvideClassInfo12GetClassInfoEPP9ITypeInfo")) {
      taken[54] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18IProvideClassInfo27GetGUIDEmP5_GUID")) {
      taken[55] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN25IConnectionPointContainer20EnumConnectionPointsEPP21IEnumConnectionPoints")) {
      taken[56] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN25IConnectionPointContainer19FindConnectionPointERK5_GUIDPP16IConnectionPoint")) {
      taken[57] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8IPersist10GetClassIDEP5_GUID")) {
      taken[58] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14IPersistStream7IsDirtyEv")) {
      taken[59] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14IPersistStream4LoadEP7IStream")) {
      taken[60] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14IPersistStream4SaveEP7IStreami")) {
      taken[61] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14IPersistStream10GetSizeMaxEP15_ULARGE_INTEGER")) {
      taken[62] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18IPersistStreamInit7InitNewEv")) {
      taken[63] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15IPersistStorage7InitNewEP8IStorage")) {
      taken[64] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15IPersistStorage4LoadEP8IStorage")) {
      taken[65] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15IPersistStorage4SaveEP8IStoragei")) {
      taken[66] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15IPersistStorage13SaveCompletedEP8IStorage")) {
      taken[67] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15IPersistStorage15HandsOffStorageEv")) {
      taken[68] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19IPersistPropertyBag4LoadEP12IPropertyBagP9IErrorLog")) {
      taken[69] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19IPersistPropertyBag4SaveEP12IPropertyBagii")) {
      taken[70] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12IPersistFile10GetCurFileEPPw")) {
      taken[71] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11IDataObject7GetDataEP12tagFORMATETCP12tagSTGMEDIUM")) {
      taken[72] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11IDataObject11GetDataHereEP12tagFORMATETCP12tagSTGMEDIUM")) {
      taken[73] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11IDataObject12QueryGetDataEP12tagFORMATETC")) {
      taken[74] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11IDataObject21GetCanonicalFormatEtcEP12tagFORMATETCS1_")) {
      taken[75] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11IDataObject7SetDataEP12tagFORMATETCP12tagSTGMEDIUMi")) {
      taken[76] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11IDataObject13EnumFormatEtcEmPP14IEnumFORMATETC")) {
      taken[77] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11IDataObject7DAdviseEP12tagFORMATETCmP11IAdviseSinkPm")) {
      taken[78] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11IDataObject9DUnadviseEm")) {
      taken[79] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11IDataObject11EnumDAdviseEPP13IEnumSTATDATA")) {
      taken[80] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[81] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[82] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[83] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[84] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[85] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[86] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[87] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  HRESULT QAxServerBase::QueryInterface(REFIID riid, void **ppvObject)
  HRESULT STDMETHODCALLTYPE QueryInterface(REFIID riid, void **ppvObject) override {
    if (taken[0]) {
      int handled = 0;
      CuteQAxServerBaseCall0 call = reinterpret_cast<CuteQAxServerBaseCall0>(taken[0]);
      HRESULT given = call(this, &riid, ppvObject, &handled);
      if (handled) return given;
    }
    return QAxServerBase::QueryInterface(riid, ppvObject);
  }

  //  ULONG QAxServerBase::AddRef()
  ULONG STDMETHODCALLTYPE AddRef() override {
    if (taken[1]) {
      int handled = 0;
      CuteQAxServerBaseCall1 call = reinterpret_cast<CuteQAxServerBaseCall1>(taken[1]);
      ULONG given = call(this, &handled);
      if (handled) return given;
    }
    return QAxServerBase::AddRef();
  }

  //  ULONG QAxServerBase::Release()
  ULONG STDMETHODCALLTYPE Release() override {
    if (taken[2]) {
      int handled = 0;
      CuteQAxServerBaseCall2 call = reinterpret_cast<CuteQAxServerBaseCall2>(taken[2]);
      ULONG given = call(this, &handled);
      if (handled) return given;
    }
    return QAxServerBase::Release();
  }

  //  IUnknown *QAxServerBase::ClientSite() const
  IUnknown *STDMETHODCALLTYPE ClientSite() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQAxServerBaseCall3 call = reinterpret_cast<CuteQAxServerBaseCall3>(taken[3]);
      void * given = call(this, &handled);
      if (handled) return static_cast<IUnknown *>(given);
    }
    return QAxServerBase::ClientSite();
  }

  //  void QAxServerBase::EmitPropertyChanged(const char *property)
  void STDMETHODCALLTYPE EmitPropertyChanged(const char *property) override {
    if (taken[4]) {
      int handled = 0;
      CuteQAxServerBaseCall4 call = reinterpret_cast<CuteQAxServerBaseCall4>(taken[4]);
      call(this, property, &handled);
      if (handled) return;
    }
    QAxServerBase::EmitPropertyChanged(property);
  }

  //  bool QAxServerBase::EmitRequestPropertyChange(const char *property)
  bool STDMETHODCALLTYPE EmitRequestPropertyChange(const char *property) override {
    if (taken[5]) {
      int handled = 0;
      CuteQAxServerBaseCall5 call = reinterpret_cast<CuteQAxServerBaseCall5>(taken[5]);
      bool given = call(this, property, &handled);
      if (handled) return given;
    }
    return QAxServerBase::EmitRequestPropertyChange(property);
  }

  //  QObject *QAxServerBase::GetQObject() const
  QObject *STDMETHODCALLTYPE GetQObject() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQAxServerBaseCall6 call = reinterpret_cast<CuteQAxServerBaseCall6>(taken[6]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QObject *>(given);
    }
    return QAxServerBase::GetQObject();
  }

  //  void QAxServerBase::ReportError(int code, const QString &src, const
  //      QString &desc, const QString &context)
  void STDMETHODCALLTYPE ReportError(int code, const QString &src, const QString &desc, const QString &context) override {
    if (taken[7]) {
      int handled = 0;
      CuteQAxServerBaseCall7 call = reinterpret_cast<CuteQAxServerBaseCall7>(taken[7]);
      call(this, code, &src, &desc, &context, &handled);
      if (handled) return;
    }
    QAxServerBase::ReportError(code, src, desc, context);
  }

  //  HRESULT QAxServerBase::GetTypeInfoCount(UINT *pctinfo)
  HRESULT STDMETHODCALLTYPE GetTypeInfoCount(UINT *pctinfo) override {
    if (taken[8]) {
      int handled = 0;
      CuteQAxServerBaseCall8 call = reinterpret_cast<CuteQAxServerBaseCall8>(taken[8]);
      HRESULT given = call(this, pctinfo, &handled);
      if (handled) return given;
    }
    return QAxServerBase::GetTypeInfoCount(pctinfo);
  }

  //  HRESULT QAxServerBase::GetTypeInfo(UINT iTInfo, LCID lcid, ITypeInfo
  //      **ppTInfo)
  HRESULT STDMETHODCALLTYPE GetTypeInfo(UINT iTInfo, LCID lcid, ITypeInfo **ppTInfo) override {
    if (taken[9]) {
      int handled = 0;
      CuteQAxServerBaseCall9 call = reinterpret_cast<CuteQAxServerBaseCall9>(taken[9]);
      HRESULT given = call(this, iTInfo, lcid, ppTInfo, &handled);
      if (handled) return given;
    }
    return QAxServerBase::GetTypeInfo(iTInfo, lcid, ppTInfo);
  }

  //  HRESULT QAxServerBase::GetIDsOfNames(REFIID riid, LPOLESTR *rgszNames,
  //      UINT cNames, LCID lcid, DISPID *rgDispId)
  HRESULT STDMETHODCALLTYPE GetIDsOfNames(REFIID riid, LPOLESTR *rgszNames, UINT cNames, LCID lcid, DISPID *rgDispId) override {
    if (taken[10]) {
      int handled = 0;
      CuteQAxServerBaseCall10 call = reinterpret_cast<CuteQAxServerBaseCall10>(taken[10]);
      HRESULT given = call(this, &riid, rgszNames, cNames, lcid, rgDispId, &handled);
      if (handled) return given;
    }
    return QAxServerBase::GetIDsOfNames(riid, rgszNames, cNames, lcid, rgDispId);
  }

  //  HRESULT QAxServerBase::Invoke(DISPID dispIdMember, REFIID riid, LCID
  //      lcid, WORD wFlags, DISPPARAMS *pDispParams, VARIANT *pVarResult,
  //      EXCEPINFO *pExcepInfo, UINT *puArgErr)
  HRESULT STDMETHODCALLTYPE Invoke(DISPID dispIdMember, REFIID riid, LCID lcid, WORD wFlags, DISPPARAMS *pDispParams, VARIANT *pVarResult, EXCEPINFO *pExcepInfo, UINT *puArgErr) override {
    if (taken[11]) {
      int handled = 0;
      CuteQAxServerBaseCall11 call = reinterpret_cast<CuteQAxServerBaseCall11>(taken[11]);
      HRESULT given = call(this, dispIdMember, &riid, lcid, wFlags, pDispParams, pVarResult, pExcepInfo, puArgErr, &handled);
      if (handled) return given;
    }
    return QAxServerBase::Invoke(dispIdMember, riid, lcid, wFlags, pDispParams, pVarResult, pExcepInfo, puArgErr);
  }

  //  HRESULT QAxServerBase::SetClientSite(IOleClientSite *pClientSite)
  HRESULT STDMETHODCALLTYPE SetClientSite(IOleClientSite *pClientSite) override {
    if (taken[12]) {
      int handled = 0;
      CuteQAxServerBaseCall12 call = reinterpret_cast<CuteQAxServerBaseCall12>(taken[12]);
      HRESULT given = call(this, pClientSite, &handled);
      if (handled) return given;
    }
    return QAxServerBase::SetClientSite(pClientSite);
  }

  //  HRESULT QAxServerBase::GetClientSite(IOleClientSite **ppClientSite)
  HRESULT STDMETHODCALLTYPE GetClientSite(IOleClientSite **ppClientSite) override {
    if (taken[13]) {
      int handled = 0;
      CuteQAxServerBaseCall13 call = reinterpret_cast<CuteQAxServerBaseCall13>(taken[13]);
      HRESULT given = call(this, ppClientSite, &handled);
      if (handled) return given;
    }
    return QAxServerBase::GetClientSite(ppClientSite);
  }

  //  HRESULT QAxServerBase::Close(DWORD dwSaveOption)
  HRESULT STDMETHODCALLTYPE Close(DWORD dwSaveOption) override {
    if (taken[14]) {
      int handled = 0;
      CuteQAxServerBaseCall14 call = reinterpret_cast<CuteQAxServerBaseCall14>(taken[14]);
      HRESULT given = call(this, dwSaveOption, &handled);
      if (handled) return given;
    }
    return QAxServerBase::Close(dwSaveOption);
  }

  //  HRESULT QAxServerBase::SetMoniker(DWORD dwWhichMoniker, IMoniker *pmk)
  HRESULT STDMETHODCALLTYPE SetMoniker(DWORD dwWhichMoniker, IMoniker *pmk) override {
    if (taken[15]) {
      int handled = 0;
      CuteQAxServerBaseCall15 call = reinterpret_cast<CuteQAxServerBaseCall15>(taken[15]);
      HRESULT given = call(this, dwWhichMoniker, pmk, &handled);
      if (handled) return given;
    }
    return QAxServerBase::SetMoniker(dwWhichMoniker, pmk);
  }

  //  HRESULT QAxServerBase::GetMoniker(DWORD dwAssign, DWORD dwWhichMoniker,
  //      IMoniker **ppmk)
  HRESULT STDMETHODCALLTYPE GetMoniker(DWORD dwAssign, DWORD dwWhichMoniker, IMoniker **ppmk) override {
    if (taken[16]) {
      int handled = 0;
      CuteQAxServerBaseCall16 call = reinterpret_cast<CuteQAxServerBaseCall16>(taken[16]);
      HRESULT given = call(this, dwAssign, dwWhichMoniker, ppmk, &handled);
      if (handled) return given;
    }
    return QAxServerBase::GetMoniker(dwAssign, dwWhichMoniker, ppmk);
  }

  //  HRESULT QAxServerBase::InitFromData(IDataObject *pDataObject, BOOL
  //      fCreation, DWORD dwReserved)
  HRESULT STDMETHODCALLTYPE InitFromData(IDataObject *pDataObject, BOOL fCreation, DWORD dwReserved) override {
    if (taken[17]) {
      int handled = 0;
      CuteQAxServerBaseCall17 call = reinterpret_cast<CuteQAxServerBaseCall17>(taken[17]);
      HRESULT given = call(this, pDataObject, fCreation, dwReserved, &handled);
      if (handled) return given;
    }
    return QAxServerBase::InitFromData(pDataObject, fCreation, dwReserved);
  }

  //  HRESULT QAxServerBase::GetClipboardData(DWORD dwReserved, IDataObject
  //      **ppDataObject)
  HRESULT STDMETHODCALLTYPE GetClipboardData(DWORD dwReserved, IDataObject **ppDataObject) override {
    if (taken[18]) {
      int handled = 0;
      CuteQAxServerBaseCall18 call = reinterpret_cast<CuteQAxServerBaseCall18>(taken[18]);
      HRESULT given = call(this, dwReserved, ppDataObject, &handled);
      if (handled) return given;
    }
    return QAxServerBase::GetClipboardData(dwReserved, ppDataObject);
  }

  //  HRESULT QAxServerBase::DoVerb(LONG iVerb, LPMSG lpmsg, IOleClientSite
  //      *pActiveSite, LONG lindex, HWND hwndParent, LPCRECT lprcPosRect)
  HRESULT STDMETHODCALLTYPE DoVerb(LONG iVerb, LPMSG lpmsg, IOleClientSite *pActiveSite, LONG lindex, HWND hwndParent, LPCRECT lprcPosRect) override {
    if (taken[19]) {
      int handled = 0;
      CuteQAxServerBaseCall19 call = reinterpret_cast<CuteQAxServerBaseCall19>(taken[19]);
      HRESULT given = call(this, iVerb, lpmsg, pActiveSite, lindex, hwndParent, lprcPosRect, &handled);
      if (handled) return given;
    }
    return QAxServerBase::DoVerb(iVerb, lpmsg, pActiveSite, lindex, hwndParent, lprcPosRect);
  }

  //  HRESULT QAxServerBase::EnumVerbs(IEnumOLEVERB **ppEnumOleVerb)
  HRESULT STDMETHODCALLTYPE EnumVerbs(IEnumOLEVERB **ppEnumOleVerb) override {
    if (taken[20]) {
      int handled = 0;
      CuteQAxServerBaseCall20 call = reinterpret_cast<CuteQAxServerBaseCall20>(taken[20]);
      HRESULT given = call(this, ppEnumOleVerb, &handled);
      if (handled) return given;
    }
    return QAxServerBase::EnumVerbs(ppEnumOleVerb);
  }

  //  HRESULT QAxServerBase::Update()
  HRESULT STDMETHODCALLTYPE Update() override {
    if (taken[21]) {
      int handled = 0;
      CuteQAxServerBaseCall21 call = reinterpret_cast<CuteQAxServerBaseCall21>(taken[21]);
      HRESULT given = call(this, &handled);
      if (handled) return given;
    }
    return QAxServerBase::Update();
  }

  //  HRESULT QAxServerBase::IsUpToDate()
  HRESULT STDMETHODCALLTYPE IsUpToDate() override {
    if (taken[22]) {
      int handled = 0;
      CuteQAxServerBaseCall22 call = reinterpret_cast<CuteQAxServerBaseCall22>(taken[22]);
      HRESULT given = call(this, &handled);
      if (handled) return given;
    }
    return QAxServerBase::IsUpToDate();
  }

  //  HRESULT QAxServerBase::GetUserClassID(CLSID *pClsid)
  HRESULT STDMETHODCALLTYPE GetUserClassID(CLSID *pClsid) override {
    if (taken[23]) {
      int handled = 0;
      CuteQAxServerBaseCall23 call = reinterpret_cast<CuteQAxServerBaseCall23>(taken[23]);
      HRESULT given = call(this, pClsid, &handled);
      if (handled) return given;
    }
    return QAxServerBase::GetUserClassID(pClsid);
  }

  //  HRESULT QAxServerBase::GetUserType(DWORD dwFormOfType, LPOLESTR
  //      *pszUserType)
  HRESULT STDMETHODCALLTYPE GetUserType(DWORD dwFormOfType, LPOLESTR *pszUserType) override {
    if (taken[24]) {
      int handled = 0;
      CuteQAxServerBaseCall24 call = reinterpret_cast<CuteQAxServerBaseCall24>(taken[24]);
      HRESULT given = call(this, dwFormOfType, pszUserType, &handled);
      if (handled) return given;
    }
    return QAxServerBase::GetUserType(dwFormOfType, pszUserType);
  }

  //  HRESULT QAxServerBase::SetExtent(DWORD dwDrawAspect, SIZEL *psizel)
  HRESULT STDMETHODCALLTYPE SetExtent(DWORD dwDrawAspect, SIZEL *psizel) override {
    if (taken[25]) {
      int handled = 0;
      CuteQAxServerBaseCall25 call = reinterpret_cast<CuteQAxServerBaseCall25>(taken[25]);
      HRESULT given = call(this, dwDrawAspect, psizel, &handled);
      if (handled) return given;
    }
    return QAxServerBase::SetExtent(dwDrawAspect, psizel);
  }

  //  HRESULT QAxServerBase::GetExtent(DWORD dwDrawAspect, SIZEL *psizel)
  HRESULT STDMETHODCALLTYPE GetExtent(DWORD dwDrawAspect, SIZEL *psizel) override {
    if (taken[26]) {
      int handled = 0;
      CuteQAxServerBaseCall26 call = reinterpret_cast<CuteQAxServerBaseCall26>(taken[26]);
      HRESULT given = call(this, dwDrawAspect, psizel, &handled);
      if (handled) return given;
    }
    return QAxServerBase::GetExtent(dwDrawAspect, psizel);
  }

  //  HRESULT QAxServerBase::Advise(IAdviseSink *pAdvSink, DWORD
  //      *pdwConnection)
  HRESULT STDMETHODCALLTYPE Advise(IAdviseSink *pAdvSink, DWORD *pdwConnection) override {
    if (taken[27]) {
      int handled = 0;
      CuteQAxServerBaseCall27 call = reinterpret_cast<CuteQAxServerBaseCall27>(taken[27]);
      HRESULT given = call(this, pAdvSink, pdwConnection, &handled);
      if (handled) return given;
    }
    return QAxServerBase::Advise(pAdvSink, pdwConnection);
  }

  //  HRESULT QAxServerBase::Unadvise(DWORD dwConnection)
  HRESULT STDMETHODCALLTYPE Unadvise(DWORD dwConnection) override {
    if (taken[28]) {
      int handled = 0;
      CuteQAxServerBaseCall28 call = reinterpret_cast<CuteQAxServerBaseCall28>(taken[28]);
      HRESULT given = call(this, dwConnection, &handled);
      if (handled) return given;
    }
    return QAxServerBase::Unadvise(dwConnection);
  }

  //  HRESULT QAxServerBase::EnumAdvise(IEnumSTATDATA **ppenumAdvise)
  HRESULT STDMETHODCALLTYPE EnumAdvise(IEnumSTATDATA **ppenumAdvise) override {
    if (taken[29]) {
      int handled = 0;
      CuteQAxServerBaseCall29 call = reinterpret_cast<CuteQAxServerBaseCall29>(taken[29]);
      HRESULT given = call(this, ppenumAdvise, &handled);
      if (handled) return given;
    }
    return QAxServerBase::EnumAdvise(ppenumAdvise);
  }

  //  HRESULT QAxServerBase::GetMiscStatus(DWORD dwAspect, DWORD *pdwStatus)
  HRESULT STDMETHODCALLTYPE GetMiscStatus(DWORD dwAspect, DWORD *pdwStatus) override {
    if (taken[30]) {
      int handled = 0;
      CuteQAxServerBaseCall30 call = reinterpret_cast<CuteQAxServerBaseCall30>(taken[30]);
      HRESULT given = call(this, dwAspect, pdwStatus, &handled);
      if (handled) return given;
    }
    return QAxServerBase::GetMiscStatus(dwAspect, pdwStatus);
  }

  //  HRESULT QAxServerBase::SetColorScheme(LOGPALETTE *pLogpal)
  HRESULT STDMETHODCALLTYPE SetColorScheme(LOGPALETTE *pLogpal) override {
    if (taken[31]) {
      int handled = 0;
      CuteQAxServerBaseCall31 call = reinterpret_cast<CuteQAxServerBaseCall31>(taken[31]);
      HRESULT given = call(this, pLogpal, &handled);
      if (handled) return given;
    }
    return QAxServerBase::SetColorScheme(pLogpal);
  }

  //  HRESULT QAxServerBase::GetControlInfo(CONTROLINFO *pCI)
  HRESULT STDMETHODCALLTYPE GetControlInfo(CONTROLINFO *pCI) override {
    if (taken[32]) {
      int handled = 0;
      CuteQAxServerBaseCall32 call = reinterpret_cast<CuteQAxServerBaseCall32>(taken[32]);
      HRESULT given = call(this, pCI, &handled);
      if (handled) return given;
    }
    return QAxServerBase::GetControlInfo(pCI);
  }

  //  HRESULT QAxServerBase::OnMnemonic(MSG *pMsg)
  HRESULT STDMETHODCALLTYPE OnMnemonic(MSG *pMsg) override {
    if (taken[33]) {
      int handled = 0;
      CuteQAxServerBaseCall33 call = reinterpret_cast<CuteQAxServerBaseCall33>(taken[33]);
      HRESULT given = call(this, pMsg, &handled);
      if (handled) return given;
    }
    return QAxServerBase::OnMnemonic(pMsg);
  }

  //  HRESULT QAxServerBase::OnAmbientPropertyChange(DISPID dispID)
  HRESULT STDMETHODCALLTYPE OnAmbientPropertyChange(DISPID dispID) override {
    if (taken[34]) {
      int handled = 0;
      CuteQAxServerBaseCall34 call = reinterpret_cast<CuteQAxServerBaseCall34>(taken[34]);
      HRESULT given = call(this, dispID, &handled);
      if (handled) return given;
    }
    return QAxServerBase::OnAmbientPropertyChange(dispID);
  }

  //  HRESULT QAxServerBase::FreezeEvents(BOOL bFreeze)
  HRESULT STDMETHODCALLTYPE FreezeEvents(BOOL bFreeze) override {
    if (taken[35]) {
      int handled = 0;
      CuteQAxServerBaseCall35 call = reinterpret_cast<CuteQAxServerBaseCall35>(taken[35]);
      HRESULT given = call(this, bFreeze, &handled);
      if (handled) return given;
    }
    return QAxServerBase::FreezeEvents(bFreeze);
  }

  //  HRESULT QAxServerBase::Draw(DWORD dwDrawAspect, LONG lindex, void
  //      *pvAspect, DVTARGETDEVICE *ptd, HDC hdcTargetDev, HDC hdcDraw,
  //      LPCRECTL lprcBounds, LPCRECTL lprcWBounds, BOOL (STDMETHODCALLTYPE
  //      *pfnContinue)(ULONG_PTR), ULONG_PTR dwContinue)
  HRESULT STDMETHODCALLTYPE Draw(DWORD dwDrawAspect, LONG lindex, void *pvAspect, DVTARGETDEVICE *ptd, HDC hdcTargetDev, HDC hdcDraw, LPCRECTL lprcBounds, LPCRECTL lprcWBounds, BOOL (STDMETHODCALLTYPE *pfnContinue)(ULONG_PTR), ULONG_PTR dwContinue) override {
    if (taken[36]) {
      int handled = 0;
      CuteQAxServerBaseCall36 call = reinterpret_cast<CuteQAxServerBaseCall36>(taken[36]);
      HRESULT given = call(this, dwDrawAspect, lindex, pvAspect, ptd, hdcTargetDev, hdcDraw, lprcBounds, lprcWBounds, reinterpret_cast<void *>(pfnContinue), dwContinue, &handled);
      if (handled) return given;
    }
    return QAxServerBase::Draw(dwDrawAspect, lindex, pvAspect, ptd, hdcTargetDev, hdcDraw, lprcBounds, lprcWBounds, pfnContinue, dwContinue);
  }

  //  HRESULT QAxServerBase::GetColorSet(DWORD dwDrawAspect, LONG lindex,
  //      void *pvAspect, DVTARGETDEVICE *ptd, HDC hicTargetDev, LOGPALETTE
  //      **ppColorSet)
  HRESULT STDMETHODCALLTYPE GetColorSet(DWORD dwDrawAspect, LONG lindex, void *pvAspect, DVTARGETDEVICE *ptd, HDC hicTargetDev, LOGPALETTE **ppColorSet) override {
    if (taken[37]) {
      int handled = 0;
      CuteQAxServerBaseCall37 call = reinterpret_cast<CuteQAxServerBaseCall37>(taken[37]);
      HRESULT given = call(this, dwDrawAspect, lindex, pvAspect, ptd, hicTargetDev, ppColorSet, &handled);
      if (handled) return given;
    }
    return QAxServerBase::GetColorSet(dwDrawAspect, lindex, pvAspect, ptd, hicTargetDev, ppColorSet);
  }

  //  HRESULT QAxServerBase::Freeze(DWORD dwDrawAspect, LONG lindex, void
  //      *pvAspect, DWORD *pdwFreeze)
  HRESULT STDMETHODCALLTYPE Freeze(DWORD dwDrawAspect, LONG lindex, void *pvAspect, DWORD *pdwFreeze) override {
    if (taken[38]) {
      int handled = 0;
      CuteQAxServerBaseCall38 call = reinterpret_cast<CuteQAxServerBaseCall38>(taken[38]);
      HRESULT given = call(this, dwDrawAspect, lindex, pvAspect, pdwFreeze, &handled);
      if (handled) return given;
    }
    return QAxServerBase::Freeze(dwDrawAspect, lindex, pvAspect, pdwFreeze);
  }

  //  HRESULT QAxServerBase::Unfreeze(DWORD dwFreeze)
  HRESULT STDMETHODCALLTYPE Unfreeze(DWORD dwFreeze) override {
    if (taken[39]) {
      int handled = 0;
      CuteQAxServerBaseCall39 call = reinterpret_cast<CuteQAxServerBaseCall39>(taken[39]);
      HRESULT given = call(this, dwFreeze, &handled);
      if (handled) return given;
    }
    return QAxServerBase::Unfreeze(dwFreeze);
  }

  //  HRESULT QAxServerBase::SetAdvise(DWORD aspects, DWORD advf, IAdviseSink
  //      *pAdvSink)
  HRESULT STDMETHODCALLTYPE SetAdvise(DWORD aspects, DWORD advf, IAdviseSink *pAdvSink) override {
    if (taken[40]) {
      int handled = 0;
      CuteQAxServerBaseCall40 call = reinterpret_cast<CuteQAxServerBaseCall40>(taken[40]);
      HRESULT given = call(this, aspects, advf, pAdvSink, &handled);
      if (handled) return given;
    }
    return QAxServerBase::SetAdvise(aspects, advf, pAdvSink);
  }

  //  HRESULT QAxServerBase::GetAdvise(DWORD *pAspects, DWORD *pAdvf,
  //      IAdviseSink **ppAdvSink)
  HRESULT STDMETHODCALLTYPE GetAdvise(DWORD *pAspects, DWORD *pAdvf, IAdviseSink **ppAdvSink) override {
    if (taken[41]) {
      int handled = 0;
      CuteQAxServerBaseCall41 call = reinterpret_cast<CuteQAxServerBaseCall41>(taken[41]);
      HRESULT given = call(this, pAspects, pAdvf, ppAdvSink, &handled);
      if (handled) return given;
    }
    return QAxServerBase::GetAdvise(pAspects, pAdvf, ppAdvSink);
  }

  //  HRESULT QAxServerBase::GetExtent(DWORD dwDrawAspect, LONG lindex,
  //      DVTARGETDEVICE *ptd, LPSIZEL lpsizel)
  HRESULT STDMETHODCALLTYPE GetExtent(DWORD dwDrawAspect, LONG lindex, DVTARGETDEVICE *ptd, LPSIZEL lpsizel) override {
    if (taken[42]) {
      int handled = 0;
      CuteQAxServerBaseCall42 call = reinterpret_cast<CuteQAxServerBaseCall42>(taken[42]);
      HRESULT given = call(this, dwDrawAspect, lindex, ptd, lpsizel, &handled);
      if (handled) return given;
    }
    return QAxServerBase::GetExtent(dwDrawAspect, lindex, ptd, lpsizel);
  }

  //  HRESULT QAxServerBase::GetWindow(HWND *phwnd)
  HRESULT STDMETHODCALLTYPE GetWindow(HWND *phwnd) override {
    if (taken[43]) {
      int handled = 0;
      CuteQAxServerBaseCall43 call = reinterpret_cast<CuteQAxServerBaseCall43>(taken[43]);
      HRESULT given = call(this, phwnd, &handled);
      if (handled) return given;
    }
    return QAxServerBase::GetWindow(phwnd);
  }

  //  HRESULT QAxServerBase::ContextSensitiveHelp(BOOL fEnterMode)
  HRESULT STDMETHODCALLTYPE ContextSensitiveHelp(BOOL fEnterMode) override {
    if (taken[44]) {
      int handled = 0;
      CuteQAxServerBaseCall44 call = reinterpret_cast<CuteQAxServerBaseCall44>(taken[44]);
      HRESULT given = call(this, fEnterMode, &handled);
      if (handled) return given;
    }
    return QAxServerBase::ContextSensitiveHelp(fEnterMode);
  }

  //  HRESULT QAxServerBase::InPlaceDeactivate()
  HRESULT STDMETHODCALLTYPE InPlaceDeactivate() override {
    if (taken[45]) {
      int handled = 0;
      CuteQAxServerBaseCall45 call = reinterpret_cast<CuteQAxServerBaseCall45>(taken[45]);
      HRESULT given = call(this, &handled);
      if (handled) return given;
    }
    return QAxServerBase::InPlaceDeactivate();
  }

  //  HRESULT QAxServerBase::UIDeactivate()
  HRESULT STDMETHODCALLTYPE UIDeactivate() override {
    if (taken[46]) {
      int handled = 0;
      CuteQAxServerBaseCall46 call = reinterpret_cast<CuteQAxServerBaseCall46>(taken[46]);
      HRESULT given = call(this, &handled);
      if (handled) return given;
    }
    return QAxServerBase::UIDeactivate();
  }

  //  HRESULT QAxServerBase::SetObjectRects(LPCRECT lprcPosRect, LPCRECT
  //      lprcClipRect)
  HRESULT STDMETHODCALLTYPE SetObjectRects(LPCRECT lprcPosRect, LPCRECT lprcClipRect) override {
    if (taken[47]) {
      int handled = 0;
      CuteQAxServerBaseCall47 call = reinterpret_cast<CuteQAxServerBaseCall47>(taken[47]);
      HRESULT given = call(this, lprcPosRect, lprcClipRect, &handled);
      if (handled) return given;
    }
    return QAxServerBase::SetObjectRects(lprcPosRect, lprcClipRect);
  }

  //  HRESULT QAxServerBase::ReactivateAndUndo()
  HRESULT STDMETHODCALLTYPE ReactivateAndUndo() override {
    if (taken[48]) {
      int handled = 0;
      CuteQAxServerBaseCall48 call = reinterpret_cast<CuteQAxServerBaseCall48>(taken[48]);
      HRESULT given = call(this, &handled);
      if (handled) return given;
    }
    return QAxServerBase::ReactivateAndUndo();
  }

  //  HRESULT QAxServerBase::TranslateAccelerator(LPMSG lpmsg)
  HRESULT STDMETHODCALLTYPE TranslateAccelerator(LPMSG lpmsg) override {
    if (taken[49]) {
      int handled = 0;
      CuteQAxServerBaseCall49 call = reinterpret_cast<CuteQAxServerBaseCall49>(taken[49]);
      HRESULT given = call(this, lpmsg, &handled);
      if (handled) return given;
    }
    return QAxServerBase::TranslateAccelerator(lpmsg);
  }

  //  HRESULT QAxServerBase::OnFrameWindowActivate(BOOL fActivate)
  HRESULT STDMETHODCALLTYPE OnFrameWindowActivate(BOOL fActivate) override {
    if (taken[50]) {
      int handled = 0;
      CuteQAxServerBaseCall50 call = reinterpret_cast<CuteQAxServerBaseCall50>(taken[50]);
      HRESULT given = call(this, fActivate, &handled);
      if (handled) return given;
    }
    return QAxServerBase::OnFrameWindowActivate(fActivate);
  }

  //  HRESULT QAxServerBase::OnDocWindowActivate(BOOL fActivate)
  HRESULT STDMETHODCALLTYPE OnDocWindowActivate(BOOL fActivate) override {
    if (taken[51]) {
      int handled = 0;
      CuteQAxServerBaseCall51 call = reinterpret_cast<CuteQAxServerBaseCall51>(taken[51]);
      HRESULT given = call(this, fActivate, &handled);
      if (handled) return given;
    }
    return QAxServerBase::OnDocWindowActivate(fActivate);
  }

  //  HRESULT QAxServerBase::ResizeBorder(LPCRECT prcBorder,
  //      IOleInPlaceUIWindow *pUIWindow, BOOL fFrameWindow)
  HRESULT STDMETHODCALLTYPE ResizeBorder(LPCRECT prcBorder, IOleInPlaceUIWindow *pUIWindow, BOOL fFrameWindow) override {
    if (taken[52]) {
      int handled = 0;
      CuteQAxServerBaseCall52 call = reinterpret_cast<CuteQAxServerBaseCall52>(taken[52]);
      HRESULT given = call(this, prcBorder, pUIWindow, fFrameWindow, &handled);
      if (handled) return given;
    }
    return QAxServerBase::ResizeBorder(prcBorder, pUIWindow, fFrameWindow);
  }

  //  HRESULT QAxServerBase::EnableModeless(BOOL fEnable)
  HRESULT STDMETHODCALLTYPE EnableModeless(BOOL fEnable) override {
    if (taken[53]) {
      int handled = 0;
      CuteQAxServerBaseCall53 call = reinterpret_cast<CuteQAxServerBaseCall53>(taken[53]);
      HRESULT given = call(this, fEnable, &handled);
      if (handled) return given;
    }
    return QAxServerBase::EnableModeless(fEnable);
  }

  //  HRESULT QAxServerBase::GetClassInfo(ITypeInfo **ppTI)
  HRESULT STDMETHODCALLTYPE GetClassInfo(ITypeInfo **ppTI) override {
    if (taken[54]) {
      int handled = 0;
      CuteQAxServerBaseCall54 call = reinterpret_cast<CuteQAxServerBaseCall54>(taken[54]);
      HRESULT given = call(this, ppTI, &handled);
      if (handled) return given;
    }
    return QAxServerBase::GetClassInfo(ppTI);
  }

  //  HRESULT QAxServerBase::GetGUID(DWORD dwGuidKind, GUID *pGUID)
  HRESULT STDMETHODCALLTYPE GetGUID(DWORD dwGuidKind, GUID *pGUID) override {
    if (taken[55]) {
      int handled = 0;
      CuteQAxServerBaseCall55 call = reinterpret_cast<CuteQAxServerBaseCall55>(taken[55]);
      HRESULT given = call(this, dwGuidKind, pGUID, &handled);
      if (handled) return given;
    }
    return QAxServerBase::GetGUID(dwGuidKind, pGUID);
  }

  //  HRESULT QAxServerBase::EnumConnectionPoints(IEnumConnectionPoints
  //      **ppEnum)
  HRESULT STDMETHODCALLTYPE EnumConnectionPoints(IEnumConnectionPoints **ppEnum) override {
    if (taken[56]) {
      int handled = 0;
      CuteQAxServerBaseCall56 call = reinterpret_cast<CuteQAxServerBaseCall56>(taken[56]);
      HRESULT given = call(this, ppEnum, &handled);
      if (handled) return given;
    }
    return QAxServerBase::EnumConnectionPoints(ppEnum);
  }

  //  HRESULT QAxServerBase::FindConnectionPoint(REFIID riid,
  //      IConnectionPoint **ppCP)
  HRESULT STDMETHODCALLTYPE FindConnectionPoint(REFIID riid, IConnectionPoint **ppCP) override {
    if (taken[57]) {
      int handled = 0;
      CuteQAxServerBaseCall57 call = reinterpret_cast<CuteQAxServerBaseCall57>(taken[57]);
      HRESULT given = call(this, &riid, ppCP, &handled);
      if (handled) return given;
    }
    return QAxServerBase::FindConnectionPoint(riid, ppCP);
  }

  //  HRESULT QAxServerBase::GetClassID(CLSID *pClassID)
  HRESULT STDMETHODCALLTYPE GetClassID(CLSID *pClassID) override {
    if (taken[58]) {
      int handled = 0;
      CuteQAxServerBaseCall58 call = reinterpret_cast<CuteQAxServerBaseCall58>(taken[58]);
      HRESULT given = call(this, pClassID, &handled);
      if (handled) return given;
    }
    return QAxServerBase::GetClassID(pClassID);
  }

  //  HRESULT QAxServerBase::IsDirty()
  HRESULT STDMETHODCALLTYPE IsDirty() override {
    if (taken[59]) {
      int handled = 0;
      CuteQAxServerBaseCall59 call = reinterpret_cast<CuteQAxServerBaseCall59>(taken[59]);
      HRESULT given = call(this, &handled);
      if (handled) return given;
    }
    return QAxServerBase::IsDirty();
  }

  //  HRESULT QAxServerBase::Load(LPSTREAM pStm)
  HRESULT STDMETHODCALLTYPE Load(LPSTREAM pStm) override {
    if (taken[60]) {
      int handled = 0;
      CuteQAxServerBaseCall60 call = reinterpret_cast<CuteQAxServerBaseCall60>(taken[60]);
      HRESULT given = call(this, pStm, &handled);
      if (handled) return given;
    }
    return QAxServerBase::Load(pStm);
  }

  //  HRESULT QAxServerBase::Save(LPSTREAM pStm, BOOL fClearDirty)
  HRESULT STDMETHODCALLTYPE Save(LPSTREAM pStm, BOOL fClearDirty) override {
    if (taken[61]) {
      int handled = 0;
      CuteQAxServerBaseCall61 call = reinterpret_cast<CuteQAxServerBaseCall61>(taken[61]);
      HRESULT given = call(this, pStm, fClearDirty, &handled);
      if (handled) return given;
    }
    return QAxServerBase::Save(pStm, fClearDirty);
  }

  //  HRESULT QAxServerBase::GetSizeMax(ULARGE_INTEGER *pCbSize)
  HRESULT STDMETHODCALLTYPE GetSizeMax(ULARGE_INTEGER *pCbSize) override {
    if (taken[62]) {
      int handled = 0;
      CuteQAxServerBaseCall62 call = reinterpret_cast<CuteQAxServerBaseCall62>(taken[62]);
      HRESULT given = call(this, pCbSize, &handled);
      if (handled) return given;
    }
    return QAxServerBase::GetSizeMax(pCbSize);
  }

  //  HRESULT QAxServerBase::InitNew()
  HRESULT STDMETHODCALLTYPE InitNew() override {
    if (taken[63]) {
      int handled = 0;
      CuteQAxServerBaseCall63 call = reinterpret_cast<CuteQAxServerBaseCall63>(taken[63]);
      HRESULT given = call(this, &handled);
      if (handled) return given;
    }
    return QAxServerBase::InitNew();
  }

  //  HRESULT QAxServerBase::InitNew(IStorage *pStg)
  HRESULT STDMETHODCALLTYPE InitNew(IStorage *pStg) override {
    if (taken[64]) {
      int handled = 0;
      CuteQAxServerBaseCall64 call = reinterpret_cast<CuteQAxServerBaseCall64>(taken[64]);
      HRESULT given = call(this, pStg, &handled);
      if (handled) return given;
    }
    return QAxServerBase::InitNew(pStg);
  }

  //  HRESULT QAxServerBase::Load(IStorage *pStg)
  HRESULT STDMETHODCALLTYPE Load(IStorage *pStg) override {
    if (taken[65]) {
      int handled = 0;
      CuteQAxServerBaseCall65 call = reinterpret_cast<CuteQAxServerBaseCall65>(taken[65]);
      HRESULT given = call(this, pStg, &handled);
      if (handled) return given;
    }
    return QAxServerBase::Load(pStg);
  }

  //  HRESULT QAxServerBase::Save(IStorage *pStgSave, BOOL fSameAsLoad)
  HRESULT STDMETHODCALLTYPE Save(IStorage *pStgSave, BOOL fSameAsLoad) override {
    if (taken[66]) {
      int handled = 0;
      CuteQAxServerBaseCall66 call = reinterpret_cast<CuteQAxServerBaseCall66>(taken[66]);
      HRESULT given = call(this, pStgSave, fSameAsLoad, &handled);
      if (handled) return given;
    }
    return QAxServerBase::Save(pStgSave, fSameAsLoad);
  }

  //  HRESULT QAxServerBase::SaveCompleted(IStorage *pStgNew)
  HRESULT STDMETHODCALLTYPE SaveCompleted(IStorage *pStgNew) override {
    if (taken[67]) {
      int handled = 0;
      CuteQAxServerBaseCall67 call = reinterpret_cast<CuteQAxServerBaseCall67>(taken[67]);
      HRESULT given = call(this, pStgNew, &handled);
      if (handled) return given;
    }
    return QAxServerBase::SaveCompleted(pStgNew);
  }

  //  HRESULT QAxServerBase::HandsOffStorage()
  HRESULT STDMETHODCALLTYPE HandsOffStorage() override {
    if (taken[68]) {
      int handled = 0;
      CuteQAxServerBaseCall68 call = reinterpret_cast<CuteQAxServerBaseCall68>(taken[68]);
      HRESULT given = call(this, &handled);
      if (handled) return given;
    }
    return QAxServerBase::HandsOffStorage();
  }

  //  HRESULT QAxServerBase::Load(IPropertyBag *pPropBag, IErrorLog
  //      *pErrorLog)
  HRESULT STDMETHODCALLTYPE Load(IPropertyBag *pPropBag, IErrorLog *pErrorLog) override {
    if (taken[69]) {
      int handled = 0;
      CuteQAxServerBaseCall69 call = reinterpret_cast<CuteQAxServerBaseCall69>(taken[69]);
      HRESULT given = call(this, pPropBag, pErrorLog, &handled);
      if (handled) return given;
    }
    return QAxServerBase::Load(pPropBag, pErrorLog);
  }

  //  HRESULT QAxServerBase::Save(IPropertyBag *pPropBag, BOOL fClearDirty,
  //      BOOL fSaveAllProperties)
  HRESULT STDMETHODCALLTYPE Save(IPropertyBag *pPropBag, BOOL fClearDirty, BOOL fSaveAllProperties) override {
    if (taken[70]) {
      int handled = 0;
      CuteQAxServerBaseCall70 call = reinterpret_cast<CuteQAxServerBaseCall70>(taken[70]);
      HRESULT given = call(this, pPropBag, fClearDirty, fSaveAllProperties, &handled);
      if (handled) return given;
    }
    return QAxServerBase::Save(pPropBag, fClearDirty, fSaveAllProperties);
  }

  //  HRESULT QAxServerBase::GetCurFile(LPOLESTR *ppszFileName)
  HRESULT STDMETHODCALLTYPE GetCurFile(LPOLESTR *ppszFileName) override {
    if (taken[71]) {
      int handled = 0;
      CuteQAxServerBaseCall71 call = reinterpret_cast<CuteQAxServerBaseCall71>(taken[71]);
      HRESULT given = call(this, ppszFileName, &handled);
      if (handled) return given;
    }
    return QAxServerBase::GetCurFile(ppszFileName);
  }

  //  HRESULT QAxServerBase::GetData(FORMATETC *pformatetcIn, STGMEDIUM
  //      *pmedium)
  HRESULT STDMETHODCALLTYPE GetData(FORMATETC *pformatetcIn, STGMEDIUM *pmedium) override {
    if (taken[72]) {
      int handled = 0;
      CuteQAxServerBaseCall72 call = reinterpret_cast<CuteQAxServerBaseCall72>(taken[72]);
      HRESULT given = call(this, pformatetcIn, pmedium, &handled);
      if (handled) return given;
    }
    return QAxServerBase::GetData(pformatetcIn, pmedium);
  }

  //  HRESULT QAxServerBase::GetDataHere(FORMATETC *pformatetc, STGMEDIUM
  //      *pmedium)
  HRESULT STDMETHODCALLTYPE GetDataHere(FORMATETC *pformatetc, STGMEDIUM *pmedium) override {
    if (taken[73]) {
      int handled = 0;
      CuteQAxServerBaseCall73 call = reinterpret_cast<CuteQAxServerBaseCall73>(taken[73]);
      HRESULT given = call(this, pformatetc, pmedium, &handled);
      if (handled) return given;
    }
    return QAxServerBase::GetDataHere(pformatetc, pmedium);
  }

  //  HRESULT QAxServerBase::QueryGetData(FORMATETC *pformatetc)
  HRESULT STDMETHODCALLTYPE QueryGetData(FORMATETC *pformatetc) override {
    if (taken[74]) {
      int handled = 0;
      CuteQAxServerBaseCall74 call = reinterpret_cast<CuteQAxServerBaseCall74>(taken[74]);
      HRESULT given = call(this, pformatetc, &handled);
      if (handled) return given;
    }
    return QAxServerBase::QueryGetData(pformatetc);
  }

  //  HRESULT QAxServerBase::GetCanonicalFormatEtc(FORMATETC *pformatectIn,
  //      FORMATETC *pformatetcOut)
  HRESULT STDMETHODCALLTYPE GetCanonicalFormatEtc(FORMATETC *pformatectIn, FORMATETC *pformatetcOut) override {
    if (taken[75]) {
      int handled = 0;
      CuteQAxServerBaseCall75 call = reinterpret_cast<CuteQAxServerBaseCall75>(taken[75]);
      HRESULT given = call(this, pformatectIn, pformatetcOut, &handled);
      if (handled) return given;
    }
    return QAxServerBase::GetCanonicalFormatEtc(pformatectIn, pformatetcOut);
  }

  //  HRESULT QAxServerBase::SetData(FORMATETC *pformatetc, STGMEDIUM
  //      *pmedium, BOOL fRelease)
  HRESULT STDMETHODCALLTYPE SetData(FORMATETC *pformatetc, STGMEDIUM *pmedium, BOOL fRelease) override {
    if (taken[76]) {
      int handled = 0;
      CuteQAxServerBaseCall76 call = reinterpret_cast<CuteQAxServerBaseCall76>(taken[76]);
      HRESULT given = call(this, pformatetc, pmedium, fRelease, &handled);
      if (handled) return given;
    }
    return QAxServerBase::SetData(pformatetc, pmedium, fRelease);
  }

  //  HRESULT QAxServerBase::EnumFormatEtc(DWORD dwDirection, IEnumFORMATETC
  //      **ppenumFormatEtc)
  HRESULT STDMETHODCALLTYPE EnumFormatEtc(DWORD dwDirection, IEnumFORMATETC **ppenumFormatEtc) override {
    if (taken[77]) {
      int handled = 0;
      CuteQAxServerBaseCall77 call = reinterpret_cast<CuteQAxServerBaseCall77>(taken[77]);
      HRESULT given = call(this, dwDirection, ppenumFormatEtc, &handled);
      if (handled) return given;
    }
    return QAxServerBase::EnumFormatEtc(dwDirection, ppenumFormatEtc);
  }

  //  HRESULT QAxServerBase::DAdvise(FORMATETC *pformatetc, DWORD advf,
  //      IAdviseSink *pAdvSink, DWORD *pdwConnection)
  HRESULT STDMETHODCALLTYPE DAdvise(FORMATETC *pformatetc, DWORD advf, IAdviseSink *pAdvSink, DWORD *pdwConnection) override {
    if (taken[78]) {
      int handled = 0;
      CuteQAxServerBaseCall78 call = reinterpret_cast<CuteQAxServerBaseCall78>(taken[78]);
      HRESULT given = call(this, pformatetc, advf, pAdvSink, pdwConnection, &handled);
      if (handled) return given;
    }
    return QAxServerBase::DAdvise(pformatetc, advf, pAdvSink, pdwConnection);
  }

  //  HRESULT QAxServerBase::DUnadvise(DWORD dwConnection)
  HRESULT STDMETHODCALLTYPE DUnadvise(DWORD dwConnection) override {
    if (taken[79]) {
      int handled = 0;
      CuteQAxServerBaseCall79 call = reinterpret_cast<CuteQAxServerBaseCall79>(taken[79]);
      HRESULT given = call(this, dwConnection, &handled);
      if (handled) return given;
    }
    return QAxServerBase::DUnadvise(dwConnection);
  }

  //  HRESULT QAxServerBase::EnumDAdvise(IEnumSTATDATA **ppenumAdvise)
  HRESULT STDMETHODCALLTYPE EnumDAdvise(IEnumSTATDATA **ppenumAdvise) override {
    if (taken[80]) {
      int handled = 0;
      CuteQAxServerBaseCall80 call = reinterpret_cast<CuteQAxServerBaseCall80>(taken[80]);
      HRESULT given = call(this, ppenumAdvise, &handled);
      if (handled) return given;
    }
    return QAxServerBase::EnumDAdvise(ppenumAdvise);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[81]) {
      int handled = 0;
      CuteQAxServerBaseCall81 call = reinterpret_cast<CuteQAxServerBaseCall81>(taken[81]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QAxServerBase::eventFilter(QObject *o, QEvent *e)
  bool eventFilter(QObject *o, QEvent *e) override {
    if (taken[82]) {
      int handled = 0;
      CuteQAxServerBaseCall82 call = reinterpret_cast<CuteQAxServerBaseCall82>(taken[82]);
      bool given = call(this, o, e, &handled);
      if (handled) return given;
    }
    return QAxServerBase::eventFilter(o, e);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[83]) {
      int handled = 0;
      CuteQAxServerBaseCall83 call = reinterpret_cast<CuteQAxServerBaseCall83>(taken[83]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[84]) {
      int handled = 0;
      CuteQAxServerBaseCall84 call = reinterpret_cast<CuteQAxServerBaseCall84>(taken[84]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[85]) {
      int handled = 0;
      CuteQAxServerBaseCall85 call = reinterpret_cast<CuteQAxServerBaseCall85>(taken[85]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[86]) {
      int handled = 0;
      CuteQAxServerBaseCall86 call = reinterpret_cast<CuteQAxServerBaseCall86>(taken[86]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[87]) {
      int handled = 0;
      CuteQAxServerBaseCall87 call = reinterpret_cast<CuteQAxServerBaseCall87>(taken[87]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  QAxServerBase::QAxServerBase(const QString &classname, IUnknown
//      *outerUnknown)
extern "C" Q_DECL_EXPORT
QAxServerBase *ritual_ZN13QAxServerBaseC1ERK7QStringP8IUnknown(
    const QString *classname,
    IUnknown *outerUnknown) {
  return new CuteQAxServerBase(*classname, outerUnknown);
}

//  QAxServerBase::QAxServerBase(QObject *o)
extern "C" Q_DECL_EXPORT
QAxServerBase *ritual_ZN13QAxServerBaseC1EP7QObject(QObject *o) {
  return new CuteQAxServerBase(o);
}

//  QAxServerBase::~QAxServerBase()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QAxServerBaseD1Ev(QAxServerBase *self) {
  delete self;
}

//  HRESULT QAxServerBase::QueryInterface(REFIID riid, void **ppvObject)
extern "C" Q_DECL_EXPORT
HRESULT ritual_ZN13QAxServerBase14QueryInterfaceERK5_GUIDPPv(
    QAxServerBase *self,
    const IID *riid,
    void **ppvObject) {
  return self->QueryInterface(*riid, ppvObject);
}

//  ULONG QAxServerBase::AddRef()
extern "C" Q_DECL_EXPORT
ULONG ritual_ZN13QAxServerBase6AddRefEv(QAxServerBase *self) {
  return self->AddRef();
}

//  ULONG QAxServerBase::Release()
extern "C" Q_DECL_EXPORT
ULONG ritual_ZN13QAxServerBase7ReleaseEv(QAxServerBase *self) {
  return self->Release();
}

//  IUnknown *QAxServerBase::ClientSite() const
extern "C" Q_DECL_EXPORT
IUnknown *ritual_ZNK13QAxServerBase10ClientSiteEv(
    const QAxServerBase *self) {
  return self->ClientSite();
}

//  void QAxServerBase::EmitPropertyChanged(const char *property)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QAxServerBase19EmitPropertyChangedEPKc(
    QAxServerBase *self,
    const char *property) {
  self->EmitPropertyChanged(property);
}

//  bool QAxServerBase::EmitRequestPropertyChange(const char *property)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QAxServerBase25EmitRequestPropertyChangeEPKc(
    QAxServerBase *self,
    const char *property) {
  return self->EmitRequestPropertyChange(property);
}

//  QObject *QAxServerBase::GetQObject() const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK13QAxServerBase10GetQObjectEv(const QAxServerBase *self) {
  return self->GetQObject();
}

//  void QAxServerBase::ReportError(int code, const QString &src, const
//      QString &desc, const QString &context)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QAxServerBase11ReportErrorEiRK7QStringS2_S2_(
    QAxServerBase *self,
    int code,
    const QString *src,
    const QString *desc,
    const QString *context) {
  self->ReportError(code, *src, *desc, *context);
}

//  HRESULT QAxServerBase::GetTypeInfoCount(UINT *pctinfo)
extern "C" Q_DECL_EXPORT
HRESULT ritual_ZN13QAxServerBase16GetTypeInfoCountEPj(
    QAxServerBase *self,
    UINT *pctinfo) {
  return self->GetTypeInfoCount(pctinfo);
}

//  HRESULT QAxServerBase::GetTypeInfo(UINT iTInfo, LCID lcid, ITypeInfo
//      **ppTInfo)
extern "C" Q_DECL_EXPORT
HRESULT ritual_ZN13QAxServerBase11GetTypeInfoEjmPP9ITypeInfo(
    QAxServerBase *self,
    UINT iTInfo,
    LCID lcid,
    ITypeInfo **ppTInfo) {
  return self->GetTypeInfo(iTInfo, lcid, ppTInfo);
}

//  HRESULT QAxServerBase::GetIDsOfNames(REFIID riid, LPOLESTR *rgszNames,
//      UINT cNames, LCID lcid, DISPID *rgDispId)
extern "C" Q_DECL_EXPORT
HRESULT ritual_ZN13QAxServerBase13GetIDsOfNamesERK5_GUIDPPwjmPl(
    QAxServerBase *self,
    const IID *riid,
    LPOLESTR *rgszNames,
    UINT cNames,
    LCID lcid,
    DISPID *rgDispId) {
  return self->GetIDsOfNames(*riid, rgszNames, cNames, lcid, rgDispId);
}

//  HRESULT QAxServerBase::Invoke(DISPID dispIdMember, REFIID riid, LCID
//      lcid, WORD wFlags, DISPPARAMS *pDispParams, VARIANT *pVarResult,
//      EXCEPINFO *pExcepInfo, UINT *puArgErr)
extern "C" Q_DECL_EXPORT
HRESULT ritual_ZN13QAxServerBase6InvokeElRK5_GUIDmtP13tagDISPPARAMSP10tagVARIANTP12tagEXCEPINFOPj(
    QAxServerBase *self,
    DISPID dispIdMember,
    const IID *riid,
    LCID lcid,
    WORD wFlags,
    DISPPARAMS *pDispParams,
    VARIANT *pVarResult,
    EXCEPINFO *pExcepInfo,
    UINT *puArgErr) {
  return self->Invoke(
      dispIdMember,
      *riid,
      lcid,
      wFlags,
      pDispParams,
      pVarResult,
      pExcepInfo,
      puArgErr);
}

//  HRESULT QAxServerBase::SetClientSite(IOleClientSite *pClientSite)
extern "C" Q_DECL_EXPORT
HRESULT ritual_ZN13QAxServerBase13SetClientSiteEP14IOleClientSite(
    QAxServerBase *self,
    IOleClientSite *pClientSite) {
  return self->SetClientSite(pClientSite);
}

//  HRESULT QAxServerBase::GetClientSite(IOleClientSite **ppClientSite)
extern "C" Q_DECL_EXPORT
HRESULT ritual_ZN13QAxServerBase13GetClientSiteEPP14IOleClientSite(
    QAxServerBase *self,
    IOleClientSite **ppClientSite) {
  return self->GetClientSite(ppClientSite);
}

//  HRESULT QAxServerBase::Close(DWORD dwSaveOption)
extern "C" Q_DECL_EXPORT
HRESULT ritual_ZN13QAxServerBase5CloseEm(
    QAxServerBase *self,
    DWORD dwSaveOption) {
  return self->Close(dwSaveOption);
}

//  HRESULT QAxServerBase::SetMoniker(DWORD dwWhichMoniker, IMoniker *pmk)
extern "C" Q_DECL_EXPORT
HRESULT ritual_ZN13QAxServerBase10SetMonikerEmP8IMoniker(
    QAxServerBase *self,
    DWORD dwWhichMoniker,
    IMoniker *pmk) {
  return self->SetMoniker(dwWhichMoniker, pmk);
}

//  HRESULT QAxServerBase::GetMoniker(DWORD dwAssign, DWORD dwWhichMoniker,
//      IMoniker **ppmk)
extern "C" Q_DECL_EXPORT
HRESULT ritual_ZN13QAxServerBase10GetMonikerEmmPP8IMoniker(
    QAxServerBase *self,
    DWORD dwAssign,
    DWORD dwWhichMoniker,
    IMoniker **ppmk) {
  return self->GetMoniker(dwAssign, dwWhichMoniker, ppmk);
}

//  HRESULT QAxServerBase::InitFromData(IDataObject *pDataObject, BOOL
//      fCreation, DWORD dwReserved)
extern "C" Q_DECL_EXPORT
HRESULT ritual_ZN13QAxServerBase12InitFromDataEP11IDataObjectim(
    QAxServerBase *self,
    IDataObject *pDataObject,
    BOOL fCreation,
    DWORD dwReserved) {
  return self->InitFromData(pDataObject, fCreation, dwReserved);
}

//  HRESULT QAxServerBase::GetClipboardData(DWORD dwReserved, IDataObject
//      **ppDataObject)
extern "C" Q_DECL_EXPORT
HRESULT ritual_ZN13QAxServerBase16GetClipboardDataEmPP11IDataObject(
    QAxServerBase *self,
    DWORD dwReserved,
    IDataObject **ppDataObject) {
  return self->GetClipboardData(dwReserved, ppDataObject);
}

//  HRESULT QAxServerBase::DoVerb(LONG iVerb, LPMSG lpmsg, IOleClientSite
//      *pActiveSite, LONG lindex, HWND hwndParent, LPCRECT lprcPosRect)
extern "C" Q_DECL_EXPORT
HRESULT ritual_ZN13QAxServerBase6DoVerbElP6tagMSGP14IOleClientSitelP6HWND__PK7tagRECT(
    QAxServerBase *self,
    LONG iVerb,
    LPMSG lpmsg,
    IOleClientSite *pActiveSite,
    LONG lindex,
    HWND hwndParent,
    LPCRECT lprcPosRect) {
  return self->DoVerb(
      iVerb, lpmsg, pActiveSite, lindex, hwndParent, lprcPosRect);
}

//  HRESULT QAxServerBase::EnumVerbs(IEnumOLEVERB **ppEnumOleVerb)
extern "C" Q_DECL_EXPORT
HRESULT ritual_ZN13QAxServerBase9EnumVerbsEPP12IEnumOLEVERB(
    QAxServerBase *self,
    IEnumOLEVERB **ppEnumOleVerb) {
  return self->EnumVerbs(ppEnumOleVerb);
}

//  HRESULT QAxServerBase::Update()
extern "C" Q_DECL_EXPORT
HRESULT ritual_ZN13QAxServerBase6UpdateEv(QAxServerBase *self) {
  return self->Update();
}

//  HRESULT QAxServerBase::IsUpToDate()
extern "C" Q_DECL_EXPORT
HRESULT ritual_ZN13QAxServerBase10IsUpToDateEv(QAxServerBase *self) {
  return self->IsUpToDate();
}

//  HRESULT QAxServerBase::GetUserClassID(CLSID *pClsid)
extern "C" Q_DECL_EXPORT
HRESULT ritual_ZN13QAxServerBase14GetUserClassIDEP5_GUID(
    QAxServerBase *self,
    CLSID *pClsid) {
  return self->GetUserClassID(pClsid);
}

//  HRESULT QAxServerBase::GetUserType(DWORD dwFormOfType, LPOLESTR
//      *pszUserType)
extern "C" Q_DECL_EXPORT
HRESULT ritual_ZN13QAxServerBase11GetUserTypeEmPPw(
    QAxServerBase *self,
    DWORD dwFormOfType,
    LPOLESTR *pszUserType) {
  return self->GetUserType(dwFormOfType, pszUserType);
}

//  HRESULT QAxServerBase::SetExtent(DWORD dwDrawAspect, SIZEL *psizel)
extern "C" Q_DECL_EXPORT
HRESULT ritual_ZN13QAxServerBase9SetExtentEmP7tagSIZE(
    QAxServerBase *self,
    DWORD dwDrawAspect,
    SIZEL *psizel) {
  return self->SetExtent(dwDrawAspect, psizel);
}

//  HRESULT QAxServerBase::GetExtent(DWORD dwDrawAspect, SIZEL *psizel)
extern "C" Q_DECL_EXPORT
HRESULT ritual_ZN13QAxServerBase9GetExtentEmP7tagSIZE(
    QAxServerBase *self,
    DWORD dwDrawAspect,
    SIZEL *psizel) {
  return self->GetExtent(dwDrawAspect, psizel);
}

//  HRESULT QAxServerBase::Advise(IAdviseSink *pAdvSink, DWORD
//      *pdwConnection)
extern "C" Q_DECL_EXPORT
HRESULT ritual_ZN13QAxServerBase6AdviseEP11IAdviseSinkPm(
    QAxServerBase *self,
    IAdviseSink *pAdvSink,
    DWORD *pdwConnection) {
  return self->Advise(pAdvSink, pdwConnection);
}

//  HRESULT QAxServerBase::Unadvise(DWORD dwConnection)
extern "C" Q_DECL_EXPORT
HRESULT ritual_ZN13QAxServerBase8UnadviseEm(
    QAxServerBase *self,
    DWORD dwConnection) {
  return self->Unadvise(dwConnection);
}

//  HRESULT QAxServerBase::EnumAdvise(IEnumSTATDATA **ppenumAdvise)
extern "C" Q_DECL_EXPORT
HRESULT ritual_ZN13QAxServerBase10EnumAdviseEPP13IEnumSTATDATA(
    QAxServerBase *self,
    IEnumSTATDATA **ppenumAdvise) {
  return self->EnumAdvise(ppenumAdvise);
}

//  HRESULT QAxServerBase::GetMiscStatus(DWORD dwAspect, DWORD *pdwStatus)
extern "C" Q_DECL_EXPORT
HRESULT ritual_ZN13QAxServerBase13GetMiscStatusEmPm(
    QAxServerBase *self,
    DWORD dwAspect,
    DWORD *pdwStatus) {
  return self->GetMiscStatus(dwAspect, pdwStatus);
}

//  HRESULT QAxServerBase::SetColorScheme(LOGPALETTE *pLogpal)
extern "C" Q_DECL_EXPORT
HRESULT ritual_ZN13QAxServerBase14SetColorSchemeEP13tagLOGPALETTE(
    QAxServerBase *self,
    LOGPALETTE *pLogpal) {
  return self->SetColorScheme(pLogpal);
}

//  HRESULT QAxServerBase::GetControlInfo(CONTROLINFO *pCI)
extern "C" Q_DECL_EXPORT
HRESULT ritual_ZN13QAxServerBase14GetControlInfoEP14tagCONTROLINFO(
    QAxServerBase *self,
    CONTROLINFO *pCI) {
  return self->GetControlInfo(pCI);
}

//  HRESULT QAxServerBase::OnMnemonic(MSG *pMsg)
extern "C" Q_DECL_EXPORT
HRESULT ritual_ZN13QAxServerBase10OnMnemonicEP6tagMSG(
    QAxServerBase *self,
    MSG *pMsg) {
  return self->OnMnemonic(pMsg);
}

//  HRESULT QAxServerBase::OnAmbientPropertyChange(DISPID dispID)
extern "C" Q_DECL_EXPORT
HRESULT ritual_ZN13QAxServerBase23OnAmbientPropertyChangeEl(
    QAxServerBase *self,
    DISPID dispID) {
  return self->OnAmbientPropertyChange(dispID);
}

//  HRESULT QAxServerBase::FreezeEvents(BOOL bFreeze)
extern "C" Q_DECL_EXPORT
HRESULT ritual_ZN13QAxServerBase12FreezeEventsEi(
    QAxServerBase *self,
    BOOL bFreeze) {
  return self->FreezeEvents(bFreeze);
}

//  HRESULT QAxServerBase::Draw(DWORD dwDrawAspect, LONG lindex, void
//      *pvAspect, DVTARGETDEVICE *ptd, HDC hdcTargetDev, HDC hdcDraw,
//      LPCRECTL lprcBounds, LPCRECTL lprcWBounds, BOOL (STDMETHODCALLTYPE
//      *pfnContinue)(ULONG_PTR), ULONG_PTR dwContinue)
extern "C" Q_DECL_EXPORT
HRESULT ritual_ZN13QAxServerBase4DrawEmlPvP17tagDVTARGETDEVICEP5HDC__S4_PK6_RECTLS7_PFiyEy(
    QAxServerBase *self,
    DWORD dwDrawAspect,
    LONG lindex,
    void *pvAspect,
    DVTARGETDEVICE *ptd,
    HDC hdcTargetDev,
    HDC hdcDraw,
    LPCRECTL lprcBounds,
    LPCRECTL lprcWBounds,
    void *pfnContinue,
    ULONG_PTR dwContinue) {
  return self->Draw(
      dwDrawAspect,
      lindex,
      pvAspect,
      ptd,
      hdcTargetDev,
      hdcDraw,
      lprcBounds,
      lprcWBounds,
      reinterpret_cast<BOOL (STDMETHODCALLTYPE *)(ULONG_PTR)>(pfnContinue),
      dwContinue);
}

//  HRESULT QAxServerBase::GetColorSet(DWORD dwDrawAspect, LONG lindex, void
//      *pvAspect, DVTARGETDEVICE *ptd, HDC hicTargetDev, LOGPALETTE
//      **ppColorSet)
extern "C" Q_DECL_EXPORT
HRESULT ritual_ZN13QAxServerBase11GetColorSetEmlPvP17tagDVTARGETDEVICEP5HDC__PP13tagLOGPALETTE(
    QAxServerBase *self,
    DWORD dwDrawAspect,
    LONG lindex,
    void *pvAspect,
    DVTARGETDEVICE *ptd,
    HDC hicTargetDev,
    LOGPALETTE **ppColorSet) {
  return self->GetColorSet(
      dwDrawAspect, lindex, pvAspect, ptd, hicTargetDev, ppColorSet);
}

//  HRESULT QAxServerBase::Freeze(DWORD dwDrawAspect, LONG lindex, void
//      *pvAspect, DWORD *pdwFreeze)
extern "C" Q_DECL_EXPORT
HRESULT ritual_ZN13QAxServerBase6FreezeEmlPvPm(
    QAxServerBase *self,
    DWORD dwDrawAspect,
    LONG lindex,
    void *pvAspect,
    DWORD *pdwFreeze) {
  return self->Freeze(dwDrawAspect, lindex, pvAspect, pdwFreeze);
}

//  HRESULT QAxServerBase::Unfreeze(DWORD dwFreeze)
extern "C" Q_DECL_EXPORT
HRESULT ritual_ZN13QAxServerBase8UnfreezeEm(
    QAxServerBase *self,
    DWORD dwFreeze) {
  return self->Unfreeze(dwFreeze);
}

//  HRESULT QAxServerBase::SetAdvise(DWORD aspects, DWORD advf, IAdviseSink
//      *pAdvSink)
extern "C" Q_DECL_EXPORT
HRESULT ritual_ZN13QAxServerBase9SetAdviseEmmP11IAdviseSink(
    QAxServerBase *self,
    DWORD aspects,
    DWORD advf,
    IAdviseSink *pAdvSink) {
  return self->SetAdvise(aspects, advf, pAdvSink);
}

//  HRESULT QAxServerBase::GetAdvise(DWORD *pAspects, DWORD *pAdvf,
//      IAdviseSink **ppAdvSink)
extern "C" Q_DECL_EXPORT
HRESULT ritual_ZN13QAxServerBase9GetAdviseEPmS0_PP11IAdviseSink(
    QAxServerBase *self,
    DWORD *pAspects,
    DWORD *pAdvf,
    IAdviseSink **ppAdvSink) {
  return self->GetAdvise(pAspects, pAdvf, ppAdvSink);
}

//  HRESULT QAxServerBase::GetExtent(DWORD dwDrawAspect, LONG lindex,
//      DVTARGETDEVICE *ptd, LPSIZEL lpsizel)
extern "C" Q_DECL_EXPORT
HRESULT ritual_ZN13QAxServerBase9GetExtentEmlP17tagDVTARGETDEVICEP7tagSIZE(
    QAxServerBase *self,
    DWORD dwDrawAspect,
    LONG lindex,
    DVTARGETDEVICE *ptd,
    LPSIZEL lpsizel) {
  return self->GetExtent(dwDrawAspect, lindex, ptd, lpsizel);
}

//  HRESULT QAxServerBase::GetWindow(HWND *phwnd)
extern "C" Q_DECL_EXPORT
HRESULT ritual_ZN13QAxServerBase9GetWindowEPP6HWND__(
    QAxServerBase *self,
    HWND *phwnd) {
  return self->GetWindow(phwnd);
}

//  HRESULT QAxServerBase::ContextSensitiveHelp(BOOL fEnterMode)
extern "C" Q_DECL_EXPORT
HRESULT ritual_ZN13QAxServerBase20ContextSensitiveHelpEi(
    QAxServerBase *self,
    BOOL fEnterMode) {
  return self->ContextSensitiveHelp(fEnterMode);
}

//  HRESULT QAxServerBase::InPlaceDeactivate()
extern "C" Q_DECL_EXPORT
HRESULT ritual_ZN13QAxServerBase17InPlaceDeactivateEv(QAxServerBase *self) {
  return self->InPlaceDeactivate();
}

//  HRESULT QAxServerBase::UIDeactivate()
extern "C" Q_DECL_EXPORT
HRESULT ritual_ZN13QAxServerBase12UIDeactivateEv(QAxServerBase *self) {
  return self->UIDeactivate();
}

//  HRESULT QAxServerBase::SetObjectRects(LPCRECT lprcPosRect, LPCRECT
//      lprcClipRect)
extern "C" Q_DECL_EXPORT
HRESULT ritual_ZN13QAxServerBase14SetObjectRectsEPK7tagRECTS2_(
    QAxServerBase *self,
    LPCRECT lprcPosRect,
    LPCRECT lprcClipRect) {
  return self->SetObjectRects(lprcPosRect, lprcClipRect);
}

//  HRESULT QAxServerBase::ReactivateAndUndo()
extern "C" Q_DECL_EXPORT
HRESULT ritual_ZN13QAxServerBase17ReactivateAndUndoEv(QAxServerBase *self) {
  return self->ReactivateAndUndo();
}

//  HRESULT QAxServerBase::TranslateAccelerator(LPMSG lpmsg)
extern "C" Q_DECL_EXPORT
HRESULT ritual_ZN13QAxServerBase20TranslateAcceleratorEP6tagMSG(
    QAxServerBase *self,
    LPMSG lpmsg) {
  return self->TranslateAccelerator(lpmsg);
}

//  HRESULT QAxServerBase::OnFrameWindowActivate(BOOL fActivate)
extern "C" Q_DECL_EXPORT
HRESULT ritual_ZN13QAxServerBase21OnFrameWindowActivateEi(
    QAxServerBase *self,
    BOOL fActivate) {
  return self->OnFrameWindowActivate(fActivate);
}

//  HRESULT QAxServerBase::OnDocWindowActivate(BOOL fActivate)
extern "C" Q_DECL_EXPORT
HRESULT ritual_ZN13QAxServerBase19OnDocWindowActivateEi(
    QAxServerBase *self,
    BOOL fActivate) {
  return self->OnDocWindowActivate(fActivate);
}

//  HRESULT QAxServerBase::ResizeBorder(LPCRECT prcBorder,
//      IOleInPlaceUIWindow *pUIWindow, BOOL fFrameWindow)
extern "C" Q_DECL_EXPORT
HRESULT ritual_ZN13QAxServerBase12ResizeBorderEPK7tagRECTP19IOleInPlaceUIWindowi(
    QAxServerBase *self,
    LPCRECT prcBorder,
    IOleInPlaceUIWindow *pUIWindow,
    BOOL fFrameWindow) {
  return self->ResizeBorder(prcBorder, pUIWindow, fFrameWindow);
}

//  HRESULT QAxServerBase::EnableModeless(BOOL fEnable)
extern "C" Q_DECL_EXPORT
HRESULT ritual_ZN13QAxServerBase14EnableModelessEi(
    QAxServerBase *self,
    BOOL fEnable) {
  return self->EnableModeless(fEnable);
}

//  HRESULT QAxServerBase::GetClassInfo(ITypeInfo **ppTI)
extern "C" Q_DECL_EXPORT
HRESULT ritual_ZN13QAxServerBase12GetClassInfoEPP9ITypeInfo(
    QAxServerBase *self,
    ITypeInfo **ppTI) {
  return self->GetClassInfo(ppTI);
}

//  HRESULT QAxServerBase::GetGUID(DWORD dwGuidKind, GUID *pGUID)
extern "C" Q_DECL_EXPORT
HRESULT ritual_ZN13QAxServerBase7GetGUIDEmP5_GUID(
    QAxServerBase *self,
    DWORD dwGuidKind,
    GUID *pGUID) {
  return self->GetGUID(dwGuidKind, pGUID);
}

//  HRESULT QAxServerBase::EnumConnectionPoints(IEnumConnectionPoints
//      **ppEnum)
extern "C" Q_DECL_EXPORT
HRESULT ritual_ZN13QAxServerBase20EnumConnectionPointsEPP21IEnumConnectionPoints(
    QAxServerBase *self,
    IEnumConnectionPoints **ppEnum) {
  return self->EnumConnectionPoints(ppEnum);
}

//  HRESULT QAxServerBase::FindConnectionPoint(REFIID riid, IConnectionPoint
//      **ppCP)
extern "C" Q_DECL_EXPORT
HRESULT ritual_ZN13QAxServerBase19FindConnectionPointERK5_GUIDPP16IConnectionPoint(
    QAxServerBase *self,
    const IID *riid,
    IConnectionPoint **ppCP) {
  return self->FindConnectionPoint(*riid, ppCP);
}

//  HRESULT QAxServerBase::GetClassID(CLSID *pClassID)
extern "C" Q_DECL_EXPORT
HRESULT ritual_ZN13QAxServerBase10GetClassIDEP5_GUID(
    QAxServerBase *self,
    CLSID *pClassID) {
  return self->GetClassID(pClassID);
}

//  HRESULT QAxServerBase::IsDirty()
extern "C" Q_DECL_EXPORT
HRESULT ritual_ZN13QAxServerBase7IsDirtyEv(QAxServerBase *self) {
  return self->IsDirty();
}

//  HRESULT QAxServerBase::Load(LPSTREAM pStm)
extern "C" Q_DECL_EXPORT
HRESULT ritual_ZN13QAxServerBase4LoadEP7IStream(
    QAxServerBase *self,
    LPSTREAM pStm) {
  return self->Load(pStm);
}

//  HRESULT QAxServerBase::Save(LPSTREAM pStm, BOOL fClearDirty)
extern "C" Q_DECL_EXPORT
HRESULT ritual_ZN13QAxServerBase4SaveEP7IStreami(
    QAxServerBase *self,
    LPSTREAM pStm,
    BOOL fClearDirty) {
  return self->Save(pStm, fClearDirty);
}

//  HRESULT QAxServerBase::GetSizeMax(ULARGE_INTEGER *pCbSize)
extern "C" Q_DECL_EXPORT
HRESULT ritual_ZN13QAxServerBase10GetSizeMaxEP15_ULARGE_INTEGER(
    QAxServerBase *self,
    ULARGE_INTEGER *pCbSize) {
  return self->GetSizeMax(pCbSize);
}

//  HRESULT QAxServerBase::InitNew()
extern "C" Q_DECL_EXPORT
HRESULT ritual_ZN13QAxServerBase7InitNewEv(QAxServerBase *self) {
  return self->InitNew();
}

//  HRESULT QAxServerBase::InitNew(IStorage *pStg)
extern "C" Q_DECL_EXPORT
HRESULT ritual_ZN13QAxServerBase7InitNewEP8IStorage(
    QAxServerBase *self,
    IStorage *pStg) {
  return self->InitNew(pStg);
}

//  HRESULT QAxServerBase::Load(IStorage *pStg)
extern "C" Q_DECL_EXPORT
HRESULT ritual_ZN13QAxServerBase4LoadEP8IStorage(
    QAxServerBase *self,
    IStorage *pStg) {
  return self->Load(pStg);
}

//  HRESULT QAxServerBase::Save(IStorage *pStgSave, BOOL fSameAsLoad)
extern "C" Q_DECL_EXPORT
HRESULT ritual_ZN13QAxServerBase4SaveEP8IStoragei(
    QAxServerBase *self,
    IStorage *pStgSave,
    BOOL fSameAsLoad) {
  return self->Save(pStgSave, fSameAsLoad);
}

//  HRESULT QAxServerBase::SaveCompleted(IStorage *pStgNew)
extern "C" Q_DECL_EXPORT
HRESULT ritual_ZN13QAxServerBase13SaveCompletedEP8IStorage(
    QAxServerBase *self,
    IStorage *pStgNew) {
  return self->SaveCompleted(pStgNew);
}

//  HRESULT QAxServerBase::HandsOffStorage()
extern "C" Q_DECL_EXPORT
HRESULT ritual_ZN13QAxServerBase15HandsOffStorageEv(QAxServerBase *self) {
  return self->HandsOffStorage();
}

//  HRESULT QAxServerBase::Load(IPropertyBag *pPropBag, IErrorLog *pErrorLog)
extern "C" Q_DECL_EXPORT
HRESULT ritual_ZN13QAxServerBase4LoadEP12IPropertyBagP9IErrorLog(
    QAxServerBase *self,
    IPropertyBag *pPropBag,
    IErrorLog *pErrorLog) {
  return self->Load(pPropBag, pErrorLog);
}

//  HRESULT QAxServerBase::Save(IPropertyBag *pPropBag, BOOL fClearDirty,
//      BOOL fSaveAllProperties)
extern "C" Q_DECL_EXPORT
HRESULT ritual_ZN13QAxServerBase4SaveEP12IPropertyBagii(
    QAxServerBase *self,
    IPropertyBag *pPropBag,
    BOOL fClearDirty,
    BOOL fSaveAllProperties) {
  return self->Save(pPropBag, fClearDirty, fSaveAllProperties);
}

//  HRESULT QAxServerBase::GetCurFile(LPOLESTR *ppszFileName)
extern "C" Q_DECL_EXPORT
HRESULT ritual_ZN13QAxServerBase10GetCurFileEPPw(
    QAxServerBase *self,
    LPOLESTR *ppszFileName) {
  return self->GetCurFile(ppszFileName);
}

//  HRESULT QAxServerBase::GetData(FORMATETC *pformatetcIn, STGMEDIUM
//      *pmedium)
extern "C" Q_DECL_EXPORT
HRESULT ritual_ZN13QAxServerBase7GetDataEP12tagFORMATETCP12tagSTGMEDIUM(
    QAxServerBase *self,
    FORMATETC *pformatetcIn,
    STGMEDIUM *pmedium) {
  return self->GetData(pformatetcIn, pmedium);
}

//  HRESULT QAxServerBase::GetDataHere(FORMATETC *pformatetc, STGMEDIUM
//      *pmedium)
extern "C" Q_DECL_EXPORT
HRESULT ritual_ZN13QAxServerBase11GetDataHereEP12tagFORMATETCP12tagSTGMEDIUM(
    QAxServerBase *self,
    FORMATETC *pformatetc,
    STGMEDIUM *pmedium) {
  return self->GetDataHere(pformatetc, pmedium);
}

//  HRESULT QAxServerBase::QueryGetData(FORMATETC *pformatetc)
extern "C" Q_DECL_EXPORT
HRESULT ritual_ZN13QAxServerBase12QueryGetDataEP12tagFORMATETC(
    QAxServerBase *self,
    FORMATETC *pformatetc) {
  return self->QueryGetData(pformatetc);
}

//  HRESULT QAxServerBase::GetCanonicalFormatEtc(FORMATETC *pformatectIn,
//      FORMATETC *pformatetcOut)
extern "C" Q_DECL_EXPORT
HRESULT ritual_ZN13QAxServerBase21GetCanonicalFormatEtcEP12tagFORMATETCS1_(
    QAxServerBase *self,
    FORMATETC *pformatectIn,
    FORMATETC *pformatetcOut) {
  return self->GetCanonicalFormatEtc(pformatectIn, pformatetcOut);
}

//  HRESULT QAxServerBase::SetData(FORMATETC *pformatetc, STGMEDIUM *pmedium,
//      BOOL fRelease)
extern "C" Q_DECL_EXPORT
HRESULT ritual_ZN13QAxServerBase7SetDataEP12tagFORMATETCP12tagSTGMEDIUMi(
    QAxServerBase *self,
    FORMATETC *pformatetc,
    STGMEDIUM *pmedium,
    BOOL fRelease) {
  return self->SetData(pformatetc, pmedium, fRelease);
}

//  HRESULT QAxServerBase::EnumFormatEtc(DWORD dwDirection, IEnumFORMATETC
//      **ppenumFormatEtc)
extern "C" Q_DECL_EXPORT
HRESULT ritual_ZN13QAxServerBase13EnumFormatEtcEmPP14IEnumFORMATETC(
    QAxServerBase *self,
    DWORD dwDirection,
    IEnumFORMATETC **ppenumFormatEtc) {
  return self->EnumFormatEtc(dwDirection, ppenumFormatEtc);
}

//  HRESULT QAxServerBase::DAdvise(FORMATETC *pformatetc, DWORD advf,
//      IAdviseSink *pAdvSink, DWORD *pdwConnection)
extern "C" Q_DECL_EXPORT
HRESULT ritual_ZN13QAxServerBase7DAdviseEP12tagFORMATETCmP11IAdviseSinkPm(
    QAxServerBase *self,
    FORMATETC *pformatetc,
    DWORD advf,
    IAdviseSink *pAdvSink,
    DWORD *pdwConnection) {
  return self->DAdvise(pformatetc, advf, pAdvSink, pdwConnection);
}

//  HRESULT QAxServerBase::DUnadvise(DWORD dwConnection)
extern "C" Q_DECL_EXPORT
HRESULT ritual_ZN13QAxServerBase9DUnadviseEm(
    QAxServerBase *self,
    DWORD dwConnection) {
  return self->DUnadvise(dwConnection);
}

//  HRESULT QAxServerBase::EnumDAdvise(IEnumSTATDATA **ppenumAdvise)
extern "C" Q_DECL_EXPORT
HRESULT ritual_ZN13QAxServerBase11EnumDAdviseEPP13IEnumSTATDATA(
    QAxServerBase *self,
    IEnumSTATDATA **ppenumAdvise) {
  return self->EnumDAdvise(ppenumAdvise);
}

//  void QAxServerBase::init()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QAxServerBase4initEv(QAxServerBase *self) {
  self->init();
}

//  HMENU QAxServerBase::createPopup(QMenu *popup, HMENU oldMenu)
extern "C" Q_DECL_EXPORT
HMENU ritual_ZN13QAxServerBase11createPopupEP5QMenuP7HMENU__(
    QAxServerBase *self,
    QMenu *popup,
    HMENU oldMenu) {
  return self->createPopup(popup, oldMenu);
}

//  void QAxServerBase::createMenu(QMenuBar *menuBar)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QAxServerBase10createMenuEP8QMenuBar(
    QAxServerBase *self,
    QMenuBar *menuBar) {
  self->createMenu(menuBar);
}

//  void QAxServerBase::removeMenu()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QAxServerBase10removeMenuEv(QAxServerBase *self) {
  self->removeMenu();
}

//  LRESULT QAxServerBase::ActiveXProc(HWND hWnd, UINT uMsg, WPARAM wParam,
//      LPARAM lParam)
extern "C" Q_DECL_EXPORT
LRESULT ritual_ZN13QAxServerBase11ActiveXProcEP6HWND__jyx(
    HWND hWnd,
    UINT uMsg,
    WPARAM wParam,
    LPARAM lParam) {
  return QAxServerBase::ActiveXProc(hWnd, uMsg, wParam, lParam);
}

//  void QAxServerBase::registerActiveObject(IUnknown *object)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QAxServerBase20registerActiveObjectEP8IUnknown(
    QAxServerBase *self,
    IUnknown *object) {
  self->registerActiveObject(object);
}

//  void QAxServerBase::revokeActiveObject()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QAxServerBase18revokeActiveObjectEv(QAxServerBase *self) {
  self->revokeActiveObject();
}

//  HRESULT QAxServerBase::InternalQueryInterface(REFIID iid, void **iface)
extern "C" Q_DECL_EXPORT
HRESULT ritual_ZN13QAxServerBase22InternalQueryInterfaceERK5_GUIDPPv(
    QAxServerBase *self,
    const IID *iid,
    void **iface) {
  return self->InternalQueryInterface(*iid, iface);
}

//  void QAxServerBase::ensureMetaData()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QAxServerBase14ensureMetaDataEv(QAxServerBase *self) {
  self->ensureMetaData();
}

//  bool QAxServerBase::isPropertyExposed(int index)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QAxServerBase17isPropertyExposedEi(
    QAxServerBase *self,
    int index) {
  return self->isPropertyExposed(index);
}

//  bool QAxServerBase::eventFilter(QObject *o, QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QAxServerBase11eventFilterEP7QObjectP6QEvent(
    QAxServerBase *self,
    QObject *o,
    QEvent *e) {
  return self->eventFilter(o, e);
}

//  RECT QAxServerBase::rcPosRect() const
extern "C" Q_DECL_EXPORT
RECT *ritual_ZNK13QAxServerBase9rcPosRectEv(const QAxServerBase *self) {
  return new RECT(self->rcPosRect());
}

//  void QAxServerBase::update()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QAxServerBase6updateEv(QAxServerBase *self) {
  self->update();
}

//  void QAxServerBase::resize(const QSize &newSize)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QAxServerBase6resizeERK5QSize(
    QAxServerBase *self,
    const QSize *newSize) {
  self->resize(*newSize);
}

//  void QAxServerBase::updateGeometry()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QAxServerBase14updateGeometryEv(QAxServerBase *self) {
  self->updateGeometry();
}

//  void QAxServerBase::updateMask()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QAxServerBase10updateMaskEv(QAxServerBase *self) {
  self->updateMask();
}

//  bool QAxServerBase::internalCreate()
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QAxServerBase14internalCreateEv(QAxServerBase *self) {
  return self->internalCreate();
}

//  void QAxServerBase::internalBind()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QAxServerBase12internalBindEv(QAxServerBase *self) {
  self->internalBind();
}

//  void QAxServerBase::internalConnect()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QAxServerBase15internalConnectEv(QAxServerBase *self) {
  self->internalConnect();
}

//  HRESULT QAxServerBase::internalActivate()
extern "C" Q_DECL_EXPORT
HRESULT ritual_ZN13QAxServerBase16internalActivateEv(QAxServerBase *self) {
  return self->internalActivate();
}

//  a Python function taken by a CuteQAxServerBase, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAxServerBase(
    QAxServerBase *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAxServerBase *>(self)->take(key, call);
}

//  HRESULT QAxServerBase::QueryInterface(REFIID riid, void **ppvObject)
extern "C" Q_DECL_EXPORT
HRESULT ritual_own_ZN13QAxServerBase14QueryInterfaceERK5_GUIDPPv(
    QAxServerBase *self,
    const IID *riid,
    void **ppvObject) {
  return self->QAxServerBase::QueryInterface(*riid, ppvObject);
}

//  ULONG QAxServerBase::AddRef()
extern "C" Q_DECL_EXPORT
ULONG ritual_own_ZN13QAxServerBase6AddRefEv(QAxServerBase *self) {
  return self->QAxServerBase::AddRef();
}

//  ULONG QAxServerBase::Release()
extern "C" Q_DECL_EXPORT
ULONG ritual_own_ZN13QAxServerBase7ReleaseEv(QAxServerBase *self) {
  return self->QAxServerBase::Release();
}

//  IUnknown *QAxServerBase::ClientSite() const
extern "C" Q_DECL_EXPORT
IUnknown *ritual_own_ZNK13QAxServerBase10ClientSiteEv(
    const QAxServerBase *self) {
  return self->QAxServerBase::ClientSite();
}

//  void QAxServerBase::EmitPropertyChanged(const char *property)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QAxServerBase19EmitPropertyChangedEPKc(
    QAxServerBase *self,
    const char *property) {
  self->QAxServerBase::EmitPropertyChanged(property);
}

//  bool QAxServerBase::EmitRequestPropertyChange(const char *property)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN13QAxServerBase25EmitRequestPropertyChangeEPKc(
    QAxServerBase *self,
    const char *property) {
  return self->QAxServerBase::EmitRequestPropertyChange(property);
}

//  QObject *QAxServerBase::GetQObject() const
extern "C" Q_DECL_EXPORT
QObject *ritual_own_ZNK13QAxServerBase10GetQObjectEv(
    const QAxServerBase *self) {
  return self->QAxServerBase::GetQObject();
}

//  void QAxServerBase::ReportError(int code, const QString &src, const
//      QString &desc, const QString &context)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QAxServerBase11ReportErrorEiRK7QStringS2_S2_(
    QAxServerBase *self,
    int code,
    const QString *src,
    const QString *desc,
    const QString *context) {
  self->QAxServerBase::ReportError(code, *src, *desc, *context);
}

//  HRESULT QAxServerBase::GetTypeInfoCount(UINT *pctinfo)
extern "C" Q_DECL_EXPORT
HRESULT ritual_own_ZN13QAxServerBase16GetTypeInfoCountEPj(
    QAxServerBase *self,
    UINT *pctinfo) {
  return self->QAxServerBase::GetTypeInfoCount(pctinfo);
}

//  HRESULT QAxServerBase::GetTypeInfo(UINT iTInfo, LCID lcid, ITypeInfo
//      **ppTInfo)
extern "C" Q_DECL_EXPORT
HRESULT ritual_own_ZN13QAxServerBase11GetTypeInfoEjmPP9ITypeInfo(
    QAxServerBase *self,
    UINT iTInfo,
    LCID lcid,
    ITypeInfo **ppTInfo) {
  return self->QAxServerBase::GetTypeInfo(iTInfo, lcid, ppTInfo);
}

//  HRESULT QAxServerBase::GetIDsOfNames(REFIID riid, LPOLESTR *rgszNames,
//      UINT cNames, LCID lcid, DISPID *rgDispId)
extern "C" Q_DECL_EXPORT
HRESULT ritual_own_ZN13QAxServerBase13GetIDsOfNamesERK5_GUIDPPwjmPl(
    QAxServerBase *self,
    const IID *riid,
    LPOLESTR *rgszNames,
    UINT cNames,
    LCID lcid,
    DISPID *rgDispId) {
  return self->QAxServerBase::GetIDsOfNames(
      *riid, rgszNames, cNames, lcid, rgDispId);
}

//  HRESULT QAxServerBase::Invoke(DISPID dispIdMember, REFIID riid, LCID
//      lcid, WORD wFlags, DISPPARAMS *pDispParams, VARIANT *pVarResult,
//      EXCEPINFO *pExcepInfo, UINT *puArgErr)
extern "C" Q_DECL_EXPORT
HRESULT ritual_own_ZN13QAxServerBase6InvokeElRK5_GUIDmtP13tagDISPPARAMSP10tagVARIANTP12tagEXCEPINFOPj(
    QAxServerBase *self,
    DISPID dispIdMember,
    const IID *riid,
    LCID lcid,
    WORD wFlags,
    DISPPARAMS *pDispParams,
    VARIANT *pVarResult,
    EXCEPINFO *pExcepInfo,
    UINT *puArgErr) {
  return self->QAxServerBase::Invoke(
      dispIdMember,
      *riid,
      lcid,
      wFlags,
      pDispParams,
      pVarResult,
      pExcepInfo,
      puArgErr);
}

//  HRESULT QAxServerBase::SetClientSite(IOleClientSite *pClientSite)
extern "C" Q_DECL_EXPORT
HRESULT ritual_own_ZN13QAxServerBase13SetClientSiteEP14IOleClientSite(
    QAxServerBase *self,
    IOleClientSite *pClientSite) {
  return self->QAxServerBase::SetClientSite(pClientSite);
}

//  HRESULT QAxServerBase::GetClientSite(IOleClientSite **ppClientSite)
extern "C" Q_DECL_EXPORT
HRESULT ritual_own_ZN13QAxServerBase13GetClientSiteEPP14IOleClientSite(
    QAxServerBase *self,
    IOleClientSite **ppClientSite) {
  return self->QAxServerBase::GetClientSite(ppClientSite);
}

//  HRESULT QAxServerBase::Close(DWORD dwSaveOption)
extern "C" Q_DECL_EXPORT
HRESULT ritual_own_ZN13QAxServerBase5CloseEm(
    QAxServerBase *self,
    DWORD dwSaveOption) {
  return self->QAxServerBase::Close(dwSaveOption);
}

//  HRESULT QAxServerBase::SetMoniker(DWORD dwWhichMoniker, IMoniker *pmk)
extern "C" Q_DECL_EXPORT
HRESULT ritual_own_ZN13QAxServerBase10SetMonikerEmP8IMoniker(
    QAxServerBase *self,
    DWORD dwWhichMoniker,
    IMoniker *pmk) {
  return self->QAxServerBase::SetMoniker(dwWhichMoniker, pmk);
}

//  HRESULT QAxServerBase::GetMoniker(DWORD dwAssign, DWORD dwWhichMoniker,
//      IMoniker **ppmk)
extern "C" Q_DECL_EXPORT
HRESULT ritual_own_ZN13QAxServerBase10GetMonikerEmmPP8IMoniker(
    QAxServerBase *self,
    DWORD dwAssign,
    DWORD dwWhichMoniker,
    IMoniker **ppmk) {
  return self->QAxServerBase::GetMoniker(dwAssign, dwWhichMoniker, ppmk);
}

//  HRESULT QAxServerBase::InitFromData(IDataObject *pDataObject, BOOL
//      fCreation, DWORD dwReserved)
extern "C" Q_DECL_EXPORT
HRESULT ritual_own_ZN13QAxServerBase12InitFromDataEP11IDataObjectim(
    QAxServerBase *self,
    IDataObject *pDataObject,
    BOOL fCreation,
    DWORD dwReserved) {
  return self->QAxServerBase::InitFromData(
      pDataObject, fCreation, dwReserved);
}

//  HRESULT QAxServerBase::GetClipboardData(DWORD dwReserved, IDataObject
//      **ppDataObject)
extern "C" Q_DECL_EXPORT
HRESULT ritual_own_ZN13QAxServerBase16GetClipboardDataEmPP11IDataObject(
    QAxServerBase *self,
    DWORD dwReserved,
    IDataObject **ppDataObject) {
  return self->QAxServerBase::GetClipboardData(dwReserved, ppDataObject);
}

//  HRESULT QAxServerBase::DoVerb(LONG iVerb, LPMSG lpmsg, IOleClientSite
//      *pActiveSite, LONG lindex, HWND hwndParent, LPCRECT lprcPosRect)
extern "C" Q_DECL_EXPORT
HRESULT ritual_own_ZN13QAxServerBase6DoVerbElP6tagMSGP14IOleClientSitelP6HWND__PK7tagRECT(
    QAxServerBase *self,
    LONG iVerb,
    LPMSG lpmsg,
    IOleClientSite *pActiveSite,
    LONG lindex,
    HWND hwndParent,
    LPCRECT lprcPosRect) {
  return self->QAxServerBase::DoVerb(
      iVerb, lpmsg, pActiveSite, lindex, hwndParent, lprcPosRect);
}

//  HRESULT QAxServerBase::EnumVerbs(IEnumOLEVERB **ppEnumOleVerb)
extern "C" Q_DECL_EXPORT
HRESULT ritual_own_ZN13QAxServerBase9EnumVerbsEPP12IEnumOLEVERB(
    QAxServerBase *self,
    IEnumOLEVERB **ppEnumOleVerb) {
  return self->QAxServerBase::EnumVerbs(ppEnumOleVerb);
}

//  HRESULT QAxServerBase::Update()
extern "C" Q_DECL_EXPORT
HRESULT ritual_own_ZN13QAxServerBase6UpdateEv(QAxServerBase *self) {
  return self->QAxServerBase::Update();
}

//  HRESULT QAxServerBase::IsUpToDate()
extern "C" Q_DECL_EXPORT
HRESULT ritual_own_ZN13QAxServerBase10IsUpToDateEv(QAxServerBase *self) {
  return self->QAxServerBase::IsUpToDate();
}

//  HRESULT QAxServerBase::GetUserClassID(CLSID *pClsid)
extern "C" Q_DECL_EXPORT
HRESULT ritual_own_ZN13QAxServerBase14GetUserClassIDEP5_GUID(
    QAxServerBase *self,
    CLSID *pClsid) {
  return self->QAxServerBase::GetUserClassID(pClsid);
}

//  HRESULT QAxServerBase::GetUserType(DWORD dwFormOfType, LPOLESTR
//      *pszUserType)
extern "C" Q_DECL_EXPORT
HRESULT ritual_own_ZN13QAxServerBase11GetUserTypeEmPPw(
    QAxServerBase *self,
    DWORD dwFormOfType,
    LPOLESTR *pszUserType) {
  return self->QAxServerBase::GetUserType(dwFormOfType, pszUserType);
}

//  HRESULT QAxServerBase::SetExtent(DWORD dwDrawAspect, SIZEL *psizel)
extern "C" Q_DECL_EXPORT
HRESULT ritual_own_ZN13QAxServerBase9SetExtentEmP7tagSIZE(
    QAxServerBase *self,
    DWORD dwDrawAspect,
    SIZEL *psizel) {
  return self->QAxServerBase::SetExtent(dwDrawAspect, psizel);
}

//  HRESULT QAxServerBase::GetExtent(DWORD dwDrawAspect, SIZEL *psizel)
extern "C" Q_DECL_EXPORT
HRESULT ritual_own_ZN13QAxServerBase9GetExtentEmP7tagSIZE(
    QAxServerBase *self,
    DWORD dwDrawAspect,
    SIZEL *psizel) {
  return self->QAxServerBase::GetExtent(dwDrawAspect, psizel);
}

//  HRESULT QAxServerBase::Advise(IAdviseSink *pAdvSink, DWORD
//      *pdwConnection)
extern "C" Q_DECL_EXPORT
HRESULT ritual_own_ZN13QAxServerBase6AdviseEP11IAdviseSinkPm(
    QAxServerBase *self,
    IAdviseSink *pAdvSink,
    DWORD *pdwConnection) {
  return self->QAxServerBase::Advise(pAdvSink, pdwConnection);
}

//  HRESULT QAxServerBase::Unadvise(DWORD dwConnection)
extern "C" Q_DECL_EXPORT
HRESULT ritual_own_ZN13QAxServerBase8UnadviseEm(
    QAxServerBase *self,
    DWORD dwConnection) {
  return self->QAxServerBase::Unadvise(dwConnection);
}

//  HRESULT QAxServerBase::EnumAdvise(IEnumSTATDATA **ppenumAdvise)
extern "C" Q_DECL_EXPORT
HRESULT ritual_own_ZN13QAxServerBase10EnumAdviseEPP13IEnumSTATDATA(
    QAxServerBase *self,
    IEnumSTATDATA **ppenumAdvise) {
  return self->QAxServerBase::EnumAdvise(ppenumAdvise);
}

//  HRESULT QAxServerBase::GetMiscStatus(DWORD dwAspect, DWORD *pdwStatus)
extern "C" Q_DECL_EXPORT
HRESULT ritual_own_ZN13QAxServerBase13GetMiscStatusEmPm(
    QAxServerBase *self,
    DWORD dwAspect,
    DWORD *pdwStatus) {
  return self->QAxServerBase::GetMiscStatus(dwAspect, pdwStatus);
}

//  HRESULT QAxServerBase::SetColorScheme(LOGPALETTE *pLogpal)
extern "C" Q_DECL_EXPORT
HRESULT ritual_own_ZN13QAxServerBase14SetColorSchemeEP13tagLOGPALETTE(
    QAxServerBase *self,
    LOGPALETTE *pLogpal) {
  return self->QAxServerBase::SetColorScheme(pLogpal);
}

//  HRESULT QAxServerBase::GetControlInfo(CONTROLINFO *pCI)
extern "C" Q_DECL_EXPORT
HRESULT ritual_own_ZN13QAxServerBase14GetControlInfoEP14tagCONTROLINFO(
    QAxServerBase *self,
    CONTROLINFO *pCI) {
  return self->QAxServerBase::GetControlInfo(pCI);
}

//  HRESULT QAxServerBase::OnMnemonic(MSG *pMsg)
extern "C" Q_DECL_EXPORT
HRESULT ritual_own_ZN13QAxServerBase10OnMnemonicEP6tagMSG(
    QAxServerBase *self,
    MSG *pMsg) {
  return self->QAxServerBase::OnMnemonic(pMsg);
}

//  HRESULT QAxServerBase::OnAmbientPropertyChange(DISPID dispID)
extern "C" Q_DECL_EXPORT
HRESULT ritual_own_ZN13QAxServerBase23OnAmbientPropertyChangeEl(
    QAxServerBase *self,
    DISPID dispID) {
  return self->QAxServerBase::OnAmbientPropertyChange(dispID);
}

//  HRESULT QAxServerBase::FreezeEvents(BOOL bFreeze)
extern "C" Q_DECL_EXPORT
HRESULT ritual_own_ZN13QAxServerBase12FreezeEventsEi(
    QAxServerBase *self,
    BOOL bFreeze) {
  return self->QAxServerBase::FreezeEvents(bFreeze);
}

//  HRESULT QAxServerBase::Draw(DWORD dwDrawAspect, LONG lindex, void
//      *pvAspect, DVTARGETDEVICE *ptd, HDC hdcTargetDev, HDC hdcDraw,
//      LPCRECTL lprcBounds, LPCRECTL lprcWBounds, BOOL (STDMETHODCALLTYPE
//      *pfnContinue)(ULONG_PTR), ULONG_PTR dwContinue)
extern "C" Q_DECL_EXPORT
HRESULT ritual_own_ZN13QAxServerBase4DrawEmlPvP17tagDVTARGETDEVICEP5HDC__S4_PK6_RECTLS7_PFiyEy(
    QAxServerBase *self,
    DWORD dwDrawAspect,
    LONG lindex,
    void *pvAspect,
    DVTARGETDEVICE *ptd,
    HDC hdcTargetDev,
    HDC hdcDraw,
    LPCRECTL lprcBounds,
    LPCRECTL lprcWBounds,
    void *pfnContinue,
    ULONG_PTR dwContinue) {
  return self->QAxServerBase::Draw(
      dwDrawAspect,
      lindex,
      pvAspect,
      ptd,
      hdcTargetDev,
      hdcDraw,
      lprcBounds,
      lprcWBounds,
      reinterpret_cast<BOOL (STDMETHODCALLTYPE *)(ULONG_PTR)>(pfnContinue),
      dwContinue);
}

//  HRESULT QAxServerBase::GetColorSet(DWORD dwDrawAspect, LONG lindex, void
//      *pvAspect, DVTARGETDEVICE *ptd, HDC hicTargetDev, LOGPALETTE
//      **ppColorSet)
extern "C" Q_DECL_EXPORT
HRESULT ritual_own_ZN13QAxServerBase11GetColorSetEmlPvP17tagDVTARGETDEVICEP5HDC__PP13tagLOGPALETTE(
    QAxServerBase *self,
    DWORD dwDrawAspect,
    LONG lindex,
    void *pvAspect,
    DVTARGETDEVICE *ptd,
    HDC hicTargetDev,
    LOGPALETTE **ppColorSet) {
  return self->QAxServerBase::GetColorSet(
      dwDrawAspect, lindex, pvAspect, ptd, hicTargetDev, ppColorSet);
}

//  HRESULT QAxServerBase::Freeze(DWORD dwDrawAspect, LONG lindex, void
//      *pvAspect, DWORD *pdwFreeze)
extern "C" Q_DECL_EXPORT
HRESULT ritual_own_ZN13QAxServerBase6FreezeEmlPvPm(
    QAxServerBase *self,
    DWORD dwDrawAspect,
    LONG lindex,
    void *pvAspect,
    DWORD *pdwFreeze) {
  return self->QAxServerBase::Freeze(
      dwDrawAspect, lindex, pvAspect, pdwFreeze);
}

//  HRESULT QAxServerBase::Unfreeze(DWORD dwFreeze)
extern "C" Q_DECL_EXPORT
HRESULT ritual_own_ZN13QAxServerBase8UnfreezeEm(
    QAxServerBase *self,
    DWORD dwFreeze) {
  return self->QAxServerBase::Unfreeze(dwFreeze);
}

//  HRESULT QAxServerBase::SetAdvise(DWORD aspects, DWORD advf, IAdviseSink
//      *pAdvSink)
extern "C" Q_DECL_EXPORT
HRESULT ritual_own_ZN13QAxServerBase9SetAdviseEmmP11IAdviseSink(
    QAxServerBase *self,
    DWORD aspects,
    DWORD advf,
    IAdviseSink *pAdvSink) {
  return self->QAxServerBase::SetAdvise(aspects, advf, pAdvSink);
}

//  HRESULT QAxServerBase::GetAdvise(DWORD *pAspects, DWORD *pAdvf,
//      IAdviseSink **ppAdvSink)
extern "C" Q_DECL_EXPORT
HRESULT ritual_own_ZN13QAxServerBase9GetAdviseEPmS0_PP11IAdviseSink(
    QAxServerBase *self,
    DWORD *pAspects,
    DWORD *pAdvf,
    IAdviseSink **ppAdvSink) {
  return self->QAxServerBase::GetAdvise(pAspects, pAdvf, ppAdvSink);
}

//  HRESULT QAxServerBase::GetExtent(DWORD dwDrawAspect, LONG lindex,
//      DVTARGETDEVICE *ptd, LPSIZEL lpsizel)
extern "C" Q_DECL_EXPORT
HRESULT ritual_own_ZN13QAxServerBase9GetExtentEmlP17tagDVTARGETDEVICEP7tagSIZE(
    QAxServerBase *self,
    DWORD dwDrawAspect,
    LONG lindex,
    DVTARGETDEVICE *ptd,
    LPSIZEL lpsizel) {
  return self->QAxServerBase::GetExtent(dwDrawAspect, lindex, ptd, lpsizel);
}

//  HRESULT QAxServerBase::GetWindow(HWND *phwnd)
extern "C" Q_DECL_EXPORT
HRESULT ritual_own_ZN13QAxServerBase9GetWindowEPP6HWND__(
    QAxServerBase *self,
    HWND *phwnd) {
  return self->QAxServerBase::GetWindow(phwnd);
}

//  HRESULT QAxServerBase::ContextSensitiveHelp(BOOL fEnterMode)
extern "C" Q_DECL_EXPORT
HRESULT ritual_own_ZN13QAxServerBase20ContextSensitiveHelpEi(
    QAxServerBase *self,
    BOOL fEnterMode) {
  return self->QAxServerBase::ContextSensitiveHelp(fEnterMode);
}

//  HRESULT QAxServerBase::InPlaceDeactivate()
extern "C" Q_DECL_EXPORT
HRESULT ritual_own_ZN13QAxServerBase17InPlaceDeactivateEv(
    QAxServerBase *self) {
  return self->QAxServerBase::InPlaceDeactivate();
}

//  HRESULT QAxServerBase::UIDeactivate()
extern "C" Q_DECL_EXPORT
HRESULT ritual_own_ZN13QAxServerBase12UIDeactivateEv(QAxServerBase *self) {
  return self->QAxServerBase::UIDeactivate();
}

//  HRESULT QAxServerBase::SetObjectRects(LPCRECT lprcPosRect, LPCRECT
//      lprcClipRect)
extern "C" Q_DECL_EXPORT
HRESULT ritual_own_ZN13QAxServerBase14SetObjectRectsEPK7tagRECTS2_(
    QAxServerBase *self,
    LPCRECT lprcPosRect,
    LPCRECT lprcClipRect) {
  return self->QAxServerBase::SetObjectRects(lprcPosRect, lprcClipRect);
}

//  HRESULT QAxServerBase::ReactivateAndUndo()
extern "C" Q_DECL_EXPORT
HRESULT ritual_own_ZN13QAxServerBase17ReactivateAndUndoEv(
    QAxServerBase *self) {
  return self->QAxServerBase::ReactivateAndUndo();
}

//  HRESULT QAxServerBase::TranslateAccelerator(LPMSG lpmsg)
extern "C" Q_DECL_EXPORT
HRESULT ritual_own_ZN13QAxServerBase20TranslateAcceleratorEP6tagMSG(
    QAxServerBase *self,
    LPMSG lpmsg) {
  return self->QAxServerBase::TranslateAccelerator(lpmsg);
}

//  HRESULT QAxServerBase::OnFrameWindowActivate(BOOL fActivate)
extern "C" Q_DECL_EXPORT
HRESULT ritual_own_ZN13QAxServerBase21OnFrameWindowActivateEi(
    QAxServerBase *self,
    BOOL fActivate) {
  return self->QAxServerBase::OnFrameWindowActivate(fActivate);
}

//  HRESULT QAxServerBase::OnDocWindowActivate(BOOL fActivate)
extern "C" Q_DECL_EXPORT
HRESULT ritual_own_ZN13QAxServerBase19OnDocWindowActivateEi(
    QAxServerBase *self,
    BOOL fActivate) {
  return self->QAxServerBase::OnDocWindowActivate(fActivate);
}

//  HRESULT QAxServerBase::ResizeBorder(LPCRECT prcBorder,
//      IOleInPlaceUIWindow *pUIWindow, BOOL fFrameWindow)
extern "C" Q_DECL_EXPORT
HRESULT ritual_own_ZN13QAxServerBase12ResizeBorderEPK7tagRECTP19IOleInPlaceUIWindowi(
    QAxServerBase *self,
    LPCRECT prcBorder,
    IOleInPlaceUIWindow *pUIWindow,
    BOOL fFrameWindow) {
  return self->QAxServerBase::ResizeBorder(
      prcBorder, pUIWindow, fFrameWindow);
}

//  HRESULT QAxServerBase::EnableModeless(BOOL fEnable)
extern "C" Q_DECL_EXPORT
HRESULT ritual_own_ZN13QAxServerBase14EnableModelessEi(
    QAxServerBase *self,
    BOOL fEnable) {
  return self->QAxServerBase::EnableModeless(fEnable);
}

//  HRESULT QAxServerBase::GetClassInfo(ITypeInfo **ppTI)
extern "C" Q_DECL_EXPORT
HRESULT ritual_own_ZN13QAxServerBase12GetClassInfoEPP9ITypeInfo(
    QAxServerBase *self,
    ITypeInfo **ppTI) {
  return self->QAxServerBase::GetClassInfo(ppTI);
}

//  HRESULT QAxServerBase::GetGUID(DWORD dwGuidKind, GUID *pGUID)
extern "C" Q_DECL_EXPORT
HRESULT ritual_own_ZN13QAxServerBase7GetGUIDEmP5_GUID(
    QAxServerBase *self,
    DWORD dwGuidKind,
    GUID *pGUID) {
  return self->QAxServerBase::GetGUID(dwGuidKind, pGUID);
}

//  HRESULT QAxServerBase::EnumConnectionPoints(IEnumConnectionPoints
//      **ppEnum)
extern "C" Q_DECL_EXPORT
HRESULT ritual_own_ZN13QAxServerBase20EnumConnectionPointsEPP21IEnumConnectionPoints(
    QAxServerBase *self,
    IEnumConnectionPoints **ppEnum) {
  return self->QAxServerBase::EnumConnectionPoints(ppEnum);
}

//  HRESULT QAxServerBase::FindConnectionPoint(REFIID riid, IConnectionPoint
//      **ppCP)
extern "C" Q_DECL_EXPORT
HRESULT ritual_own_ZN13QAxServerBase19FindConnectionPointERK5_GUIDPP16IConnectionPoint(
    QAxServerBase *self,
    const IID *riid,
    IConnectionPoint **ppCP) {
  return self->QAxServerBase::FindConnectionPoint(*riid, ppCP);
}

//  HRESULT QAxServerBase::GetClassID(CLSID *pClassID)
extern "C" Q_DECL_EXPORT
HRESULT ritual_own_ZN13QAxServerBase10GetClassIDEP5_GUID(
    QAxServerBase *self,
    CLSID *pClassID) {
  return self->QAxServerBase::GetClassID(pClassID);
}

//  HRESULT QAxServerBase::IsDirty()
extern "C" Q_DECL_EXPORT
HRESULT ritual_own_ZN13QAxServerBase7IsDirtyEv(QAxServerBase *self) {
  return self->QAxServerBase::IsDirty();
}

//  HRESULT QAxServerBase::Load(LPSTREAM pStm)
extern "C" Q_DECL_EXPORT
HRESULT ritual_own_ZN13QAxServerBase4LoadEP7IStream(
    QAxServerBase *self,
    LPSTREAM pStm) {
  return self->QAxServerBase::Load(pStm);
}

//  HRESULT QAxServerBase::Save(LPSTREAM pStm, BOOL fClearDirty)
extern "C" Q_DECL_EXPORT
HRESULT ritual_own_ZN13QAxServerBase4SaveEP7IStreami(
    QAxServerBase *self,
    LPSTREAM pStm,
    BOOL fClearDirty) {
  return self->QAxServerBase::Save(pStm, fClearDirty);
}

//  HRESULT QAxServerBase::GetSizeMax(ULARGE_INTEGER *pCbSize)
extern "C" Q_DECL_EXPORT
HRESULT ritual_own_ZN13QAxServerBase10GetSizeMaxEP15_ULARGE_INTEGER(
    QAxServerBase *self,
    ULARGE_INTEGER *pCbSize) {
  return self->QAxServerBase::GetSizeMax(pCbSize);
}

//  HRESULT QAxServerBase::InitNew()
extern "C" Q_DECL_EXPORT
HRESULT ritual_own_ZN13QAxServerBase7InitNewEv(QAxServerBase *self) {
  return self->QAxServerBase::InitNew();
}

//  HRESULT QAxServerBase::InitNew(IStorage *pStg)
extern "C" Q_DECL_EXPORT
HRESULT ritual_own_ZN13QAxServerBase7InitNewEP8IStorage(
    QAxServerBase *self,
    IStorage *pStg) {
  return self->QAxServerBase::InitNew(pStg);
}

//  HRESULT QAxServerBase::Load(IStorage *pStg)
extern "C" Q_DECL_EXPORT
HRESULT ritual_own_ZN13QAxServerBase4LoadEP8IStorage(
    QAxServerBase *self,
    IStorage *pStg) {
  return self->QAxServerBase::Load(pStg);
}

//  HRESULT QAxServerBase::Save(IStorage *pStgSave, BOOL fSameAsLoad)
extern "C" Q_DECL_EXPORT
HRESULT ritual_own_ZN13QAxServerBase4SaveEP8IStoragei(
    QAxServerBase *self,
    IStorage *pStgSave,
    BOOL fSameAsLoad) {
  return self->QAxServerBase::Save(pStgSave, fSameAsLoad);
}

//  HRESULT QAxServerBase::SaveCompleted(IStorage *pStgNew)
extern "C" Q_DECL_EXPORT
HRESULT ritual_own_ZN13QAxServerBase13SaveCompletedEP8IStorage(
    QAxServerBase *self,
    IStorage *pStgNew) {
  return self->QAxServerBase::SaveCompleted(pStgNew);
}

//  HRESULT QAxServerBase::HandsOffStorage()
extern "C" Q_DECL_EXPORT
HRESULT ritual_own_ZN13QAxServerBase15HandsOffStorageEv(
    QAxServerBase *self) {
  return self->QAxServerBase::HandsOffStorage();
}

//  HRESULT QAxServerBase::Load(IPropertyBag *pPropBag, IErrorLog *pErrorLog)
extern "C" Q_DECL_EXPORT
HRESULT ritual_own_ZN13QAxServerBase4LoadEP12IPropertyBagP9IErrorLog(
    QAxServerBase *self,
    IPropertyBag *pPropBag,
    IErrorLog *pErrorLog) {
  return self->QAxServerBase::Load(pPropBag, pErrorLog);
}

//  HRESULT QAxServerBase::Save(IPropertyBag *pPropBag, BOOL fClearDirty,
//      BOOL fSaveAllProperties)
extern "C" Q_DECL_EXPORT
HRESULT ritual_own_ZN13QAxServerBase4SaveEP12IPropertyBagii(
    QAxServerBase *self,
    IPropertyBag *pPropBag,
    BOOL fClearDirty,
    BOOL fSaveAllProperties) {
  return self->QAxServerBase::Save(
      pPropBag, fClearDirty, fSaveAllProperties);
}

//  HRESULT QAxServerBase::GetCurFile(LPOLESTR *ppszFileName)
extern "C" Q_DECL_EXPORT
HRESULT ritual_own_ZN13QAxServerBase10GetCurFileEPPw(
    QAxServerBase *self,
    LPOLESTR *ppszFileName) {
  return self->QAxServerBase::GetCurFile(ppszFileName);
}

//  HRESULT QAxServerBase::GetData(FORMATETC *pformatetcIn, STGMEDIUM
//      *pmedium)
extern "C" Q_DECL_EXPORT
HRESULT ritual_own_ZN13QAxServerBase7GetDataEP12tagFORMATETCP12tagSTGMEDIUM(
    QAxServerBase *self,
    FORMATETC *pformatetcIn,
    STGMEDIUM *pmedium) {
  return self->QAxServerBase::GetData(pformatetcIn, pmedium);
}

//  HRESULT QAxServerBase::GetDataHere(FORMATETC *pformatetc, STGMEDIUM
//      *pmedium)
extern "C" Q_DECL_EXPORT
HRESULT ritual_own_ZN13QAxServerBase11GetDataHereEP12tagFORMATETCP12tagSTGMEDIUM(
    QAxServerBase *self,
    FORMATETC *pformatetc,
    STGMEDIUM *pmedium) {
  return self->QAxServerBase::GetDataHere(pformatetc, pmedium);
}

//  HRESULT QAxServerBase::QueryGetData(FORMATETC *pformatetc)
extern "C" Q_DECL_EXPORT
HRESULT ritual_own_ZN13QAxServerBase12QueryGetDataEP12tagFORMATETC(
    QAxServerBase *self,
    FORMATETC *pformatetc) {
  return self->QAxServerBase::QueryGetData(pformatetc);
}

//  HRESULT QAxServerBase::GetCanonicalFormatEtc(FORMATETC *pformatectIn,
//      FORMATETC *pformatetcOut)
extern "C" Q_DECL_EXPORT
HRESULT ritual_own_ZN13QAxServerBase21GetCanonicalFormatEtcEP12tagFORMATETCS1_(
    QAxServerBase *self,
    FORMATETC *pformatectIn,
    FORMATETC *pformatetcOut) {
  return self->QAxServerBase::GetCanonicalFormatEtc(
      pformatectIn, pformatetcOut);
}

//  HRESULT QAxServerBase::SetData(FORMATETC *pformatetc, STGMEDIUM *pmedium,
//      BOOL fRelease)
extern "C" Q_DECL_EXPORT
HRESULT ritual_own_ZN13QAxServerBase7SetDataEP12tagFORMATETCP12tagSTGMEDIUMi(
    QAxServerBase *self,
    FORMATETC *pformatetc,
    STGMEDIUM *pmedium,
    BOOL fRelease) {
  return self->QAxServerBase::SetData(pformatetc, pmedium, fRelease);
}

//  HRESULT QAxServerBase::EnumFormatEtc(DWORD dwDirection, IEnumFORMATETC
//      **ppenumFormatEtc)
extern "C" Q_DECL_EXPORT
HRESULT ritual_own_ZN13QAxServerBase13EnumFormatEtcEmPP14IEnumFORMATETC(
    QAxServerBase *self,
    DWORD dwDirection,
    IEnumFORMATETC **ppenumFormatEtc) {
  return self->QAxServerBase::EnumFormatEtc(dwDirection, ppenumFormatEtc);
}

//  HRESULT QAxServerBase::DAdvise(FORMATETC *pformatetc, DWORD advf,
//      IAdviseSink *pAdvSink, DWORD *pdwConnection)
extern "C" Q_DECL_EXPORT
HRESULT ritual_own_ZN13QAxServerBase7DAdviseEP12tagFORMATETCmP11IAdviseSinkPm(
    QAxServerBase *self,
    FORMATETC *pformatetc,
    DWORD advf,
    IAdviseSink *pAdvSink,
    DWORD *pdwConnection) {
  return self->QAxServerBase::DAdvise(
      pformatetc, advf, pAdvSink, pdwConnection);
}

//  HRESULT QAxServerBase::DUnadvise(DWORD dwConnection)
extern "C" Q_DECL_EXPORT
HRESULT ritual_own_ZN13QAxServerBase9DUnadviseEm(
    QAxServerBase *self,
    DWORD dwConnection) {
  return self->QAxServerBase::DUnadvise(dwConnection);
}

//  HRESULT QAxServerBase::EnumDAdvise(IEnumSTATDATA **ppenumAdvise)
extern "C" Q_DECL_EXPORT
HRESULT ritual_own_ZN13QAxServerBase11EnumDAdviseEPP13IEnumSTATDATA(
    QAxServerBase *self,
    IEnumSTATDATA **ppenumAdvise) {
  return self->QAxServerBase::EnumDAdvise(ppenumAdvise);
}

//  bool QAxServerBase::eventFilter(QObject *o, QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN13QAxServerBase11eventFilterEP7QObjectP6QEvent(
    QAxServerBase *self,
    QObject *o,
    QEvent *e) {
  return self->QAxServerBase::eventFilter(o, e);
}

#endif  // defined(Q_OS_WIN)
